---
gerado: sincronizacao
---

# dbo.vwReqMsgTotal

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReqMsg` | int |
| `idThread` | int |
| `idReq` | int |
| `idTpMsg` | int |
| `dsTpMsg` | varchar |
| `dsAssunto` | varchar |
| `dsMsg` | text |
| `idRemetente` | int |
| `idResposta` | int |
| `idReqHist` | int |
| `flgPublico` | bit |
| `dtEnvioMsg` | datetime |
| `idReqHistRelac` | int |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
