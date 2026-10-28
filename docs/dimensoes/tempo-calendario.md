---
gerado: sincronizacao
---
# Dimensão: calendário de atendimento


## 1. O que é na tela

O calendário de atendimento define em que dias e em que faixas de horário um grupo atende. O BDesk o usa para medir prazos e tempos em minutos úteis: os campos `...Cal` de [Tempo da requisição](../fatos/tempo-requisicao.md), `nIntervaloCal` de [Tempo por status](../fatos/tempo-por-status.md) e `Req.sla` ([Marcos](../fatos/marcos.md)).

## 2. Estrutura

| Tabela | Papel | Chaves e colunas |
|---|---|---|
| `CalendarioNome` | o calendário (cabeçalho) | `idCan` (chave), `dsCan` (nome), `flgCanAtivo` |
| `Calendario` | as regras do calendário | `idCal` (chave), `idCan` → `CalendarioNome`, `diaSemana`, `dtCal`, `hInicio1`/`hFim1`, `hInicio2`/`hFim2`, `hInicio3`/`hFim3` |
| `Grupo` | liga o grupo ao calendário | `Grupo.idCan` → `CalendarioNome.idCan` |
| `Parametro` | calendário padrão | a linha `idPar = 15`, em `valorPar`, guarda o `idCan` do calendário padrão |
| `Feriado` | cadastro de feriados | `idFer`, `dsFer`, `dia`, `mes`, `flgMovel` |
| `CalendarioUpdate` | fila de recálculo | `idCan` ou `idGru`, `dtCriacao`, `dtExecucao` |

Cada calendário tem dois tipos de linha em `Calendario`:

- **Dia da semana:** `diaSemana` preenchido (o valor de `DATEPART(dw)`, que depende do `SET DATEFIRST` da sessão que executa o cálculo) e `dtCal` vazia, com até três faixas de horário no dia (`hInicio1` a `hFim3`, texto `HH:mm`). O fim às 23h59 vale até a meia-noite.
- **Data específica:** `dtCal` preenchida e `diaSemana` vazio. Sem horário (`hInicio1` vazio), o dia não é útil. Quando existe linha de data específica para o dia, ela prevalece sobre a linha do dia da semana.

Como o cálculo funciona: o cálculo de minutos úteis soma, dia a dia, a interseção entre o intervalo e as faixas do dia no calendário do grupo (`Grupo.idCan`); sem grupo, usa o calendário padrão (`Parametro` `idPar = 15`). Uma variante faz o mesmo recebendo o calendário diretamente. O resultado está em minutos.

## 3. Como a requisição aponta para ele

A requisição não aponta para o calendário. O caminho é pelo grupo: `Req.idGruAtual` → `Grupo.idGru` → `Grupo.idCan`. O cálculo de tempos escolhe o calendário conforme a medida:

- `tAtivoCal` e `tFreezeCal` (da requisição e de `ReqTimeAdo`): o grupo do participante de cada trecho do histórico, quando o participante é do tipo Grupo; qualquer participante que não seja do tipo Grupo usa o calendário padrão (`Parametro` `idPar = 15`);
- `tRespCal`: o grupo de quem respondeu, com a mesma regra; na encerrada sem `dtResposta`, o grupo atual da requisição (`idGruAtual`) ou o calendário padrão quando não há grupo atual;
- `tAtrasoCal`, `tAvancoCal`, `tAtrasoRealCal`, `tAvancoRealCal` e o intervalo final, do último registro do histórico até `dtCalc`: o grupo atual da requisição (`idGruAtual`), ou o calendário padrão quando a requisição não tem grupo atual.

`Grupo.idCan` sempre tem valor: a coluna não admite vazio.

O SLA gravado em `Req.sla` usa o calendário do grupo do momento do cálculo:

- **Abertura:** o grupo solicitado (`idGru`); sem grupo, o calendário padrão.
- **Categorização:** a categorização recebe o SLA pronto, calcula `dtFimPrev` no calendário do grupo solicitado a partir desse SLA e grava `sla` e, em `idGruAtual`, o grupo solicitado; ela não calcula o SLA.
- **Ações que recalculam o prazo:** ao alterar o prazo (ação `ALTPRZ`) e ao repriorizar (ação `REPRI`, que também recebe novas datas previstas), o produto valida o SLA, calculando-o no calendário de `idGruAtual`, e o grava. Na alteração de prioridade (ação `ALTPRI`), quando ela recalcula o SLA, o produto obtém `sla` pela fórmula do SLA da atividade, que não usa calendário (o grupo só escolhe o tempo-base de `TarefaGrupo`), e calcula `dtFimPrev` no calendário de `idGruAtual`; os dois só são gravados quando o SLA mudou. O recálculo por calendário ou grupo usa `idGruAtual` e, sem grupo, o calendário padrão (`idPar = 15`). Na transição de status, quando a requisição sai de um status de congelamento definitivo, o produto soma ao `sla` o tempo passado nesse status e recalcula as datas previstas no calendário de `idGruAtual`. Ao reagendar (ação `REAGE`), o produto grava o `sla` que recebe, e ao recategorizar (ação `RECAT`) grava o `sla` que recebe só quando recalcula o prazo; nenhuma das duas ações grava `idGruAtual`.

Depois de um direcionamento sem recálculo, `sla` continua no calendário do grupo anterior.

## 4. Ativo/inativo

`CalendarioNome.flgCanAtivo` indica se o calendário está ativo.

## 5. Valores do produto

Esta dimensão não tem valores definidos pelo produto em [Valores definidos pelo produto](../dominios-do-produto.md).

## 6. Regras de uso

#### R-tempo-calendario-01: Chegue ao calendário de atraso, de avanço e do intervalo final por `idGruAtual` → `Grupo.idCan`; `Req.sla` segue o grupo do momento do cálculo. {#r-tempo-calendario-01}
O calendário pertence ao grupo; a requisição tem o grupo atual em `Req.idGruAtual` e `ReqConcluida.idGruAtual`. Para `tAtivoCal` e `tFreezeCal`, o calendário é o do grupo do participante de cada trecho (tipo Grupo) ou o padrão (qualquer outro tipo de participante); `tRespCal` segue a mesma regra no histórico da primeira resposta e, na encerrada sem `dtResposta`, usa `idGruAtual` ou, sem grupo atual, o padrão. `Req.sla` segue o calendário do grupo do momento do cálculo (abertura, categorização ou ações que recalculam o prazo), como descrito na seção 3.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-calendario-02: Entenda um dia não útil como uma linha de `Calendario` com `dtCal` preenchida e sem horário. {#r-tempo-calendario-02}
É assim que o cálculo de minutos úteis reconhece o dia sem expediente, e a linha da data tem prioridade sobre a do dia da semana. A tela de calendário grava essas linhas.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-calendario-03: Leia `Feriado` como o cadastro de feriados que alimenta `Calendario`. {#r-tempo-calendario-03}
O produto copia `Feriado` para `Calendario` sob demanda: o usuário escolhe o ano, os calendários e os feriados, e entram só os feriados com `flgMovel = 0`, como linhas de data com horário vazio (`hInicio1 IS NULL` marca o dia como feriado). No banco, só o log de alterações de feriado referencia a tabela. Os cálculos de prazo e de minutos úteis leem só `Calendario`; uma data de exceção vale por `Calendario.dtCal`.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-calendario-04: Entenda que a alteração de calendário ou de grupo recalcula as requisições abertas afetadas. {#r-tempo-calendario-04}
A alteração das faixas ou datas de um calendário e a troca do calendário de um grupo gravam a fila `CalendarioUpdate`: a primeira por um gatilho do banco, quando as linhas de `Calendario` mudam, e a segunda pela tela de cadastro de grupo. Uma rotina agendada processa a fila e recalcula `Req.sla` ou `dtFimPrev`, apaga as linhas de `ReqTime` e `ReqTimeAdo` da requisição e recria o plano de alertas.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

## 7. Views recomendadas

Nenhuma. A dimensão é consultada pelas tabelas desta página.

## 8. Receitas

- [Tempo total por requisição](../receitas/tempo-total-por-requisicao.md)
- [Tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

## Veja também

- [Tempo da requisição](../fatos/tempo-requisicao.md)
- [Marcos da requisição](../fatos/marcos.md)
- [Prioridade e SLA](prioridade-sla.md)
