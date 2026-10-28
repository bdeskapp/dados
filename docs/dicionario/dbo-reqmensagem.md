---
gerado: sincronizacao
---

# dbo.ReqMensagem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqMsg` | INT | não | sim | não |
| `idThread` | INT | sim | não | não |
| `idReq` | INT | não | não | não |
| `idTpMsg` | INT | não | não | não |
| `dsAssunto` | VARCHAR(100) | não | não | não |
| `dsMsg` | TEXT | não | não | não |
| `idRemetente` | INT | não | não | não |
| `idResposta` | INT | sim | não | não |
| `idReqHist` | INT | sim | não | não |
| `flgPublico` | BIT | não | não | não |
| `dtEnvioMsg` | DATETIME | não | não | não |
| `idReqHistRelac` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqMensagem` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMensagem` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMensagem` (idReqHistRelac) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMensagem` (idResposta) → `dbo.ReqMensagem` (idReqMsg)
- `dbo.ReqMensagem` (idThread) → `dbo.ReqMensagem` (idReqMsg)
- `dbo.ReqMensagem` (idRemetente) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqMensagem` (idTpMsg) → `dbo.TipoMensagem` (idTpMsg)
- `dbo.ReqMsgAcesso` (idReqMsg) → `dbo.ReqMensagem` (idReqMsg)
