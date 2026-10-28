---
gerado: sincronizacao
---

# dbo.ReqMsgConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqMsg` | INT | não | sim | não |
| `idThread` | INT | não | não | não |
| `idReq` | INT | não | não | não |
| `idTpMsg` | INT | não | não | não |
| `dsTpMsg` | VARCHAR(40) | não | não | não |
| `dsAssunto` | VARCHAR(100) | não | não | não |
| `dsMsg` | TEXT | não | não | não |
| `idRemetente` | INT | não | não | não |
| `idResposta` | INT | sim | não | não |
| `idReqHist` | INT | sim | não | não |
| `flgPublico` | BIT | não | não | não |
| `dtEnvioMsg` | DATETIME | não | não | não |
| `idReqHistRelac` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqMsgAcessoConcluida` (idReqMsg) → `dbo.ReqMsgConcluida` (idReqMsg)
- `dbo.ReqMsgConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqMsgConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqMsgConcluida` (idReqHistRelac) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqMsgConcluida` (idResposta) → `dbo.ReqMsgConcluida` (idReqMsg)
- `dbo.ReqMsgConcluida` (idThread) → `dbo.ReqMsgConcluida` (idReqMsg)
- `dbo.ReqMsgConcluida` (idRemetente) → `dbo.ReqPartConcluida` (idReqPart)
