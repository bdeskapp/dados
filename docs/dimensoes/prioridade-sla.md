---
gerado: sincronizacao
---
# Dimensão: prioridade e SLA


## 1. O que é na tela

A prioridade é o grau de criticidade da requisição, calculado a partir do impacto e da urgência informados ou escolhido pelo atendente na ação Alterar Prioridade (`ALTPRI`). O SLA é o prazo de atendimento em minutos de calendário, que dá origem às datas `dtIniPrev` e `dtFimPrev` ([Marcos](../fatos/marcos.md)).

## 2. Estrutura

| Objeto | O que é | Chaves e colunas |
|---|---|---|
| `Req.nPrioridade` / `ReqConcluida.nPrioridade` | prioridade da requisição | `tinyint`, sem chave estrangeira |
| `Req.nImp`, `Req.nUrg` (e as de `ReqConcluida`) | nível de impacto e de urgência informados na requisição | `tinyint`, sem chave estrangeira; podem estar vazios |
| `Impacto` / `ImpactoNivel` | definição de impacto e seus níveis | `Impacto.idImp`, `dsImp`, `flgAtivo`; `ImpactoNivel` (`idImp`, `nImpNivel`) com `dsImpNivel` |
| `Urgencia` / `UrgenciaNivel` | definição de urgência e seus níveis | `Urgencia.idUrg`, `dsUrg`, `flgAtivo`; `UrgenciaNivel` (`idUrg`, `nUrgNivel`) com `dsUrgNivel` |
| `FormPri` | configuração de prioridade do formulário | chave `idFrm`; `idImp` e `idUrg` escolhem a definição de impacto e de urgência do formulário; `nPesoMatriz`, `nPesoAtividade`, `nPesoIC` e os limites `nPriBaixa`, `nPriMedia`, `nPriAlta` |
| `FormPriMatriz` | matriz impacto × urgência do formulário | chave (`idFrm`, `nImp`, `nUrg`); `valorPri` |
| `TipoSla` | tipo de SLA | `idTpSla`, `dsTpSla`, `flgTpSlaAtivo`; referenciado por `Tarefa.idTpSla` e `Fluxo.idTpSla` |
| `FormSLA` | ações do formulário que recalculam o prazo | chave (`idFrm`, `cdAcao`); `flgCalcDtIni` |
| `ReqPlanoAlerta` | plano de alertas por percentual do SLA | `idReq`, `nPerc`, `dtPrevisto`, `flgProcessado` |

- **Níveis de impacto e urgência.** `Req.nImp` guarda o número do nível; o rótulo está em `ImpactoNivel.dsImpNivel`, na definição de impacto do formulário da requisição: `Req.idFrm` → `FormPri.idFrm` → `FormPri.idImp` → `ImpactoNivel` por (`idImp`, `nImpNivel = Req.nImp`). O mesmo vale para a urgência, por `FormPri.idUrg`. O mesmo número de nível pode ter rótulos diferentes em definições diferentes.
- **Cálculo da prioridade.** O cálculo lê `valorPri` da matriz do formulário para o par (`nImp`, `nUrg`), combina com a criticidade da atividade (`Tarefa.tpCriticidade`) e a do papel de item de configuração (IC), aplica os pesos de `FormPri` e compara o resultado com os limites `nPriBaixa` e `nPriMedia`; `nPriAlta` é lido, mas não entra na comparação. Na ação `ALTPRI`, o atendente escolhe a prioridade diretamente.
- **Cálculo do SLA da atividade.** A fórmula do SLA é usada na alteração de prioridade e na validação do SLA e ao carregar o SLA da atividade. A fórmula é `tempo-base × percentual de acesso do solicitante × percentual de criticidade`, arredondado. O tempo-base é `TarefaGrupo.SlaGru`, quando o grupo tem valor para a atividade, ou `Tarefa.slaTarPadrao`; o percentual de acesso vem de `TarefaAcesso.prcSLA` (100 quando o solicitante não tem regra); o percentual de criticidade é `prcAlta`, `prcMedia` ou `prcBaixa` de `FormCategoria`, conforme a criticidade ou a prioridade informada; um SLA fixo de `TarefaAcesso.Sla` prevalece quando é menor que o resultado e também quando o resultado do cálculo é 0.
- **SLA na abertura.** A abertura escolhe o cálculo conforme `Tarefa.idTpSla` (o nome de cada tipo de SLA vem do cadastro, `TipoSla.dsTpSla`, por decisão do produto; no domínio do produto, `idTpSla` tem as chaves 0 e 1). Com `idTpSla = 1`, ou sem atividade (`idTar = 0`), e conforme a data que a abertura pede para recalcular, `dtFimPrev` é calculada a partir de `dtIniPrev` e do SLA recebido, no calendário do grupo, ou `dtIniPrev` é calculada. Com `idTpSla <> 1` ou sem atividade (`idTar = 0`), e sem planejamento do fluxo, o SLA é calculado a partir das datas, no calendário do grupo quando há grupo e no calendário padrão quando não há. Na ação `ENVAV`, o SLA passa a ser o prazo mínimo do formulário e `dtFimPrev` é calculada a partir da data atual. O prazo mínimo é `Formulario.nPrazoMinimo`; na centralizadora de um processo que usa o prazo mínimo, o SLA da abertura é esse valor. Quando o SLA calculado fica abaixo do prazo mínimo, a abertura devolve o erro `err2307`.
- **Recálculo por calendário ou grupo.** Para as requisições abertas do calendário ou do grupo informado, o recálculo trata dois casos. Nas requisições sem atividade ou com `Tarefa.idTpSla = 0`, recalcula `Req.sla` a partir das datas previstas, no calendário de `idGruAtual` (sem grupo, no calendário padrão, `idPar = 15`). Nas requisições com `Tarefa.idTpSla = 1`, recalcula `dtFimPrev` a partir do SLA, ou `dtIniPrev` nos agendamentos de prazo máximo; `tpAgend` vazio recebe o tratamento do agendamento normal. Nos dois casos, o recálculo apaga os tempos gravados da requisição em `ReqTime` e `ReqTimeAdo` e recria o plano de alertas.
- **`FormSLA`.** Marca, por formulário e código de ação, as ações que recalculam o prazo. A tabela é consultada pelo código da ação na alteração de prioridade (ação `ALTPRI`) e na recategorização (ação `RECAT`), nas duas interfaces do produto. Se o formulário tem a linha da ação, ela recalcula o SLA.
- **`flgForaSLA`.** Flag em `Req` (e `ReqConcluida.flgForaSla`) gravada ao criar o plano de alertas, com 1 quando `dtFimPrev` já passou, o que acontece na abertura, em outras ações e nos recálculos por calendário ou grupo; e gravada no processamento dos alertas, com 1 quando o alerta de 100% é processado e com 0 nos demais. Uma atualização de versão do produto (a 8.0.3) também a regrava com 0. O plano está em `ReqPlanoAlerta`. A flag retrata a última dessas gravações; no encerramento, o valor é copiado para `ReqConcluida.flgForaSla`.

## 3. Como a requisição aponta para ela

| Informação | Coluna | Observação |
|---|---|---|
| Prioridade | `Req.nPrioridade`, `ReqConcluida.nPrioridade` | valor gravado na requisição; `tinyint` sem chave estrangeira |
| Impacto e urgência | `nImp`, `nUrg` | podem vir vazios |
| Prazo | `dtIniPrev`, `dtFimPrev`, `sla` | ver [Marcos](../fatos/marcos.md) |
| Tipo de SLA | `Req.idTar` → `Tarefa.idTpSla` → `TipoSla` | a atividade (`idTar`) pode faltar |

## 4. Ativo/inativo

`Impacto.flgAtivo` e `Urgencia.flgAtivo` indicam definições ativas; `TipoSla.flgTpSlaAtivo` indica o tipo ativo.

## 5. Valores do produto

Os valores de `nPrioridade` (`1` Alta, `2` Média, `3` Baixa) são os de [Valores definidos pelo produto](../dominios-do-produto.md), seção `Req.nPrioridade`: os rótulos vêm do log de alterações da requisição, as ações `HIGH`, `MEDIUM` e `LOW` gravam 1, 2 e 3 e o cálculo pela matriz devolve os mesmos números. Os códigos de ação citados (`ALTPRI`, `RECAT`) são os de [Valores definidos pelo produto](../dominios-do-produto.md).

## 6. Regras de uso

#### R-prioridade-sla-01: Leia o rótulo do nível de impacto e de urgência pela definição do formulário. {#r-prioridade-sla-01}
`Req.nImp` e `Req.nUrg` guardam o número do nível; o rótulo está em `ImpactoNivel` e `UrgenciaNivel`, na definição indicada por `FormPri.idImp` e `FormPri.idUrg` do formulário da requisição.
Receita: [SLA por grupo](../receitas/sla-por-grupo.md)

#### R-prioridade-sla-02: Trate `nPrioridade`, `nImp` e `nUrg` como números sem chave estrangeira. {#r-prioridade-sla-02}
São `tinyint` em `Req` e `ReqConcluida`, ligados às tabelas de apoio apenas pelo cruzamento descrito na seção 2; `nImp` e `nUrg` podem estar vazios.

#### R-prioridade-sla-03: Meça "estourou o prazo" pelas datas previstas. {#r-prioridade-sla-03}
Compare `dtFimPrev` com `dtFimReal` (encerradas) ou com o momento da consulta (abertas). `flgForaSLA` é atualizada na criação do plano de alertas e no processamento do alerta, e retrata a última gravação (uma atualização de versão do produto também a regrava com 0).
Receita: [atrasadas agora](../receitas/atrasadas-agora.md)

#### R-prioridade-sla-04: Leia `sla` como minutos de calendário do grupo. {#r-prioridade-sla-04}
`Req.sla` e `ReqConcluida.Sla` medem o intervalo previsto no calendário do grupo ([Calendário](tempo-calendario.md)); `SLAOrig` guarda o SLA da abertura ou, depois de uma categorização, o da categorização: é gravado na abertura e regravado com o valor de `sla` na categorização. As demais ações que alteram `sla` (`ALTPRI`, alteração de prazo, recálculo por calendário ou grupo) não o tocam.
Receita: [SLA por grupo](../receitas/sla-por-grupo.md)

## 7. Views recomendadas

Nenhuma. A dimensão é consultada pelas tabelas desta página.

## 8. Receitas

- [SLA por grupo](../receitas/sla-por-grupo.md)
- [Atrasadas agora](../receitas/atrasadas-agora.md)

## Veja também

- [Marcos da requisição](../fatos/marcos.md)
- [Calendário de atendimento](tempo-calendario.md)
- [Tempo da requisição](../fatos/tempo-requisicao.md)
