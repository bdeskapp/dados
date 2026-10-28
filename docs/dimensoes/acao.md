---
gerado: sincronizacao
---
# Dimensão: ação


## 1. O que é na tela

A **ação** é o que o usuário executa sobre uma requisição: direcionar, atribuir, recategorizar, concluir, encerrar, acompanhar e assim por diante. Cada ação executada vira uma linha no histórico da requisição (`ReqHistorico` nas abertas e `ReqHistConcluida` nas encerradas). O botão e o texto mostrados ao usuário podem ser o rótulo do **formulário** (`FormAcao.dsAcao`).

## 2. Estrutura

```
ReqHistorico.idFrmAcao --> FormAcao.idFrmAcao --> FormAcao.idAcao --> Acao.idAcao --> Acao.cdAcao
                           (um conjunto por formulário)               (catálogo)
```

| Tabela | O que guarda | Chaves |
|---|---|---|
| `Acao` | catálogo de ações: código (`cdAcao`), rótulo do catálogo (`dsAcao`) e `flgSistema` (1 = definida pelo produto) | `idAcao` |
| `FormAcao` | as ações **de cada formulário**: liga `idFrm` a `idAcao` e traz o rótulo do formulário (`dsAcao`) | `idFrmAcao` |
| `FormTransicao` | ação (`idFrmAcao`) + status atual leva a um próximo status ([Status](status-fase.md), seção 5) | `idFrmTrans` |

- O histórico guarda `idFrmAcao`; só `ReqHistorico` tem a chave estrangeira, e `ReqHistConcluida` guarda a coluna sem chave estrangeira. O código da ação se alcança por `FormAcao → Acao.cdAcao`.
- `FormAcao.dsAcao` é o rótulo **naquele formulário** e pode diferir de `Acao.dsAcao`. O texto exibido na tela pode ser o do formulário.
- `ReqHistConcluida` guarda `dsAcao`, o rótulo gravado no encerramento.
- Entre as ações definidas pelo produto, `cdAcao` identifica uma linha. As ações criadas pela instalação têm `flgSistema = 0` e recebem um código fixo, gravado pela tela de cadastro, que por isso se repete entre elas.

## 3. Como a requisição aponta para a ação

A requisição não guarda a "ação atual": o que existe é o histórico. Cada linha de `ReqHistorico` / `ReqHistConcluida` traz `idReqHist`, `idReq`, `idFrmAcao`, `idUsu` (quem executou), `idGru`, `idFrmStatus` (status da linha) e `dtFimReqHist` (data exibida no histórico). O detalhe do histórico está em [Fato: eventos do histórico](../fatos/eventos-historico.md). A coluna `idFrmAcao` aceita vazio no esquema das duas tabelas de histórico; ligue `FormAcao` com `LEFT JOIN` para manter todas as linhas.

## 4. Valores do produto

Os valores definidos pelo produto (origem: nome fixo no produto, atualização de versão do produto ou `flgSistema = 1`) estão em [Valores definidos pelo produto](../dominios-do-produto.md), seção "Acao". As ações que o produto reconhece pelo código, com o rótulo do catálogo:

| `cdAcao` | Rótulo em `Acao.dsAcao` |
|---|---|
| `DIR` | Direcionar Requisição |
| `RECAT` | Recategorizar |
| `ENC` | Encerrar Requisição |
| `VINC` | Vincular Requisição |
| `AVAL` | Avaliar |
| `DEVD` | Devolver Direto |
| `ATR` | Atribuir Responsabilidade |
| `ATRR` | Atribuir Responsável |
| `ALTPRI` | Alterar Prioridade |
| `ALTDES` | Alterar Descrição |
| `ENV_AIR` | Enviar para o AIR |
| `ENC_EXT` | Encerrar Externo |
| `CANC_AIR` | Cancelar e encerrar no AIR |
| `ENV_OFTR` | Enviar para o OfficeTrack |
| `CANC_EXT` | Cancelar no Bdesk e APIs |

Note que `ATR` tem o rótulo "Atribuir Responsabilidade" e `ATRR` o rótulo "Atribuir Responsável"; o nome interno de cada uma dessas ações no produto não acompanha o rótulo do catálogo.

### Vocabulário

Leitura de cada código adotada nesta documentação (decisão do produto).

| Código | Rótulo do catálogo | Leitura |
|---|---|---|
| `DIR` | Direcionar Requisição | direciona a requisição; **mudança de grupo** é cada ação `DIR` registrada no histórico |
| `ENC`, `ENC_EXT` | Encerrar Requisição, Encerrar Externo | ações do catálogo que o produto reconhece pelo código |
| `CONC` | Concluir Requisição | conclusão da requisição, com o mesmo efeito de `ENC` (encerra quando leva a status final; só o rótulo muda); pode ser rejeitada pela ação `REJCON` |
| `REJCON` | Rejeitar Conclusão | **rejeição de conclusão** é cada ocorrência de `REJCON`; o status resultante vem de `FormTransicao`, e a rejeição pode deixar a requisição encerrada, conforme a transição do formulário (`FormTransicao`) |
| `RECAT` | Recategorizar | muda a atividade (`Req.idTar`); ver [Classificação](classificacao.md) |

## 5. Ação e encerramento

A ação sozinha não move a requisição para `ReqConcluida`. O produto executa a ação, `FormTransicao` indica o próximo status e, quando esse status é terminal (sem transição de saída), o produto encerra a requisição ([Status](status-fase.md), seção 5). A ação que leva ao status terminal depende do formulário. Por isso o último histórico de uma encerrada pode ser de qualquer ação (`CONC`, `ENC`, `CANC` e outras). `CONC` e `ENC` têm o mesmo efeito (encerram quando levam a status final) e só o rótulo muda (decisão do produto).

## 6. Ativo e inativo

`Acao.flgAcaoAtiva` e `FormAcao.flgDisponivel` marcam o que está ativo e disponível. `Acao.flgAcaoAtiva = 0` é a exclusão lógica da ação; as listas de ações da tela filtram `FormAcao.flgDisponivel = 1`. O histórico mantém as ações já executadas.

## 7. Regras de uso

#### R-acao-01: Leia o código da ação por `ReqHistorico.idFrmAcao → FormAcao.idAcao → Acao.cdAcao`. {#r-acao-01}
O histórico guarda a ação do formulário; para as ações do produto (`flgSistema = 1`), o código do catálogo identifica a ação em todos os formulários. As ações criadas pela instalação (`flgSistema = 0`) recebem todas o mesmo código fixo, gravado pela tela de cadastro; para elas identifique a ação por `FormAcao.idAcao`.

#### R-acao-02: Leia o texto exibido da ação em `FormAcao.dsAcao` e o texto do catálogo em `Acao.dsAcao`. {#r-acao-02}
Os dois podem diferir; a encerrada guarda o texto do formulário em `ReqHistConcluida.dsAcao`.

#### R-acao-03: Conte mudança de grupo como cada ação `DIR` do histórico e rejeição de conclusão como cada ação `REJCON`. {#r-acao-03}
Definições adotadas (decisão do produto). Some `ReqHistorico` e `ReqHistConcluida` para cobrir abertas e encerradas; uma rejeição de conclusão pode ser o último evento de uma requisição já encerrada, e `FormTransicao` informa o status que ela produz.

#### R-acao-04: Leia "quem encerrou" como o autor da ação que levou a requisição ao status terminal. {#r-acao-04}
O encerramento depende do status de destino. Quem encerrou é o autor (`idUsu`) do último histórico antes da passagem para `ReqConcluida`, qualquer que seja a ação (decisão do produto). Receita: [quem encerrou](../receitas/quem-encerrou.md).

#### R-acao-05: Leia `ATR` como "Atribuir Responsabilidade" e `ATRR` como "Atribuir Responsável" no catálogo. {#r-acao-05}
O código `cdAcao` é a chave e o rótulo do catálogo é `Acao.dsAcao`; o nome interno dessas ações no produto não acompanha o rótulo.

## 8. Views recomendadas

Nenhuma view entra para a pergunta "o que é uma ação": a página recomenda `ReqHistorico`, `ReqHistConcluida`, `FormAcao` e `Acao`.

## 9. Receitas

As receitas que usam ações (mudanças de grupo, rejeições de conclusão, quem encerrou) estão em [rejeições de conclusão](../receitas/rejeicoes-de-conclusao.md), [mudanças de grupo](../receitas/mudancas-de-grupo.md), [quem encerrou](../receitas/quem-encerrou.md) e nas páginas de eventos.

## Veja também

- [Status](status-fase.md)
- [Classificação](classificacao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
