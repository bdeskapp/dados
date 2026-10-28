---
gerado: sincronizacao
---
# Fato: tempo de atendimento por grupo


## 1. O que mede

Quanto tempo cada atendente de uma requisição ficou com ela, depois da primeira resposta, separado em tempo ativo (status que conta no SLA) e tempo em status que não conta. Com o grupo do atendente, responde "quanto tempo cada grupo ficou com as requisições".

## 2. Granularidade

Uma linha por requisição × participação (`idReqPart`): a participação que constava como atendente (`ReqHistorico.idReqPartADO`) nos registros de histórico a partir de `dtResposta`. Uma requisição que passou por mais de um atendente ou grupo tem mais de uma linha. Ao final do cálculo de tempos, é criada também a linha do atendente atual (participação `ADO` vigente) quando há `dtResposta`, mesmo que ele não tenha trecho de histórico. A chave é (`idReq`, `idReqPart`). Requisição sem `dtResposta` fica sem linhas.

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `ReqTimeAdo` | |
| Encerrada | `ReqTimeAdoConcluida` | copiada de `ReqTimeAdo` no encerramento |
| Ambas | `ReqTimeAdo` e `ReqTimeAdoConcluida` | somadas por `UNION ALL` (R-tempo-por-grupo-02) |
| Participação | `ReqParticipante` / `ReqPartConcluida` | `idReqPart` da linha de tempo aponta para a participação ([Fato: participação](participacao.md)) |
| Grupo | `Grupo` | `ReqParticipante.idPart` quando `idTpPapel = 2` |

- **Chave de grupo.** As tabelas de tempo por atendente guardam `idReqPart` como única ligação com quem atendeu. O grupo é o `idPart` dessa participação quando o tipo (`idTpPapel`) é Grupo, valor `2` em `TipoPapel`. Quando o tipo é Usuário (`1`), a linha pertence a um usuário e fica sem grupo.
- **Quem grava.** As linhas de `ReqTimeAdo` são gravadas junto com `ReqTime`, nos mesmos momentos descritos em [Tempo da requisição](tempo-requisicao.md): a cada registro de histórico, no encerramento e no lote. O encerramento copia as linhas para `ReqTimeAdoConcluida`.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReq` | requisição | |
| `idReqPart` | participação (atendente) à qual o tempo pertence | |
| `dtCalc` | momento do cálculo | data e hora |
| `tAtivo` / `tAtivoCal` | tempo do atendente em status que conta no SLA | minutos corridos / minutos do calendário |
| `tFreeze` / `tFreezeCal` | tempo do atendente em status que não conta no SLA | minutos corridos / minutos do calendário |

A soma de `tAtivoCal + tFreezeCal` das linhas de uma requisição é o `tAtendCal` dela em `ReqTime` / `ReqTimeConcluida`. O tempo até a primeira resposta (`tRespCal`) está em `ReqTime` / `ReqTimeConcluida`, fora desta tabela.

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Grupo | `idReqPart` → `ReqParticipante.idReqPart` (ou `ReqPartConcluida`); com `idTpPapel = 2`, `idPart` → `Grupo.idGru` |
| Usuário | com `idTpPapel = 1`, `idPart` → `Usuario.idUsu` |
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Tempo total | `ReqTime` / `ReqTimeConcluida`, por `idReq` ([Tempo da requisição](tempo-requisicao.md)) |

## 6. Regras de uso

#### R-tempo-por-grupo-01: Leia o grupo em `ReqParticipante.idPart` quando `idTpPapel = 2`. {#r-tempo-por-grupo-01}
`ReqTimeAdo` tem `idReqPart`, e a participação diz o tipo do participante e o destino de `idPart` ([R-participacao-03](participacao.md)). Para as encerradas, use `ReqPartConcluida`.
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

#### R-tempo-por-grupo-02: Some `ReqTimeAdo` e `ReqTimeAdoConcluida` para qualquer histórico. {#r-tempo-por-grupo-02}
A primeira guarda as requisições abertas e a segunda as encerradas.
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

#### R-tempo-por-grupo-03: Leia o tempo por grupo em `ReqTimeAdo`, cujo grão é requisição × participação (`idReqPart`). {#r-tempo-por-grupo-03}
Cada linha de `ReqTimeAdo` é o tempo de uma participação (chave `idReq`, `idReqPart`). Para o tempo de um grupo, junte `idReqPart` à participação de tipo Grupo (R-tempo-por-grupo-01) e some `tAtivoCal` e `tFreezeCal` por `idPart`. `ReqTime` guarda o tempo da requisição inteira, em uma linha por requisição (chave `idReq`).
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

#### R-tempo-por-grupo-04: Junte a linha de tempo à participação por `idReqPart` e confirme `ReqParticipante.idReq = ReqTimeAdo.idReq`. {#r-tempo-por-grupo-04}
No cálculo em lote, uma linha de `ReqTimeAdo` pode apontar para a participação de outra requisição; o filtro `ReqParticipante.idReq = ReqTimeAdo.idReq` mantém só as linhas coerentes.
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

#### R-tempo-por-grupo-05: Entenda o tempo de atendimento como o tempo posterior à primeira resposta. {#r-tempo-por-grupo-05}
As linhas nascem a partir de `dtResposta`. O tempo antes da resposta está em `tResp` / `tRespCal` de `ReqTime`.
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

## 7. Views recomendadas

Esta página recomenda as tabelas `ReqTimeAdo` e `ReqTimeAdoConcluida`. Elas guardam, por atendente, `tAtivoCal` e `tFreezeCal` em minutos do calendário e `tAtivo` e `tFreeze` em minutos corridos; para chegar ao grupo, junte `idReqPart` à participação (R-tempo-por-grupo-01). O tempo até a primeira resposta está em `ReqTime.tRespCal` ([Tempo da requisição](tempo-requisicao.md)).

## 8. Receitas

- [Tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

## Veja também

- [Tempo da requisição](tempo-requisicao.md)
- [Fato: participação](participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
