---
gerado: sincronizacao
---

# dbo.ReqStatusConcluida

**Selo:** Explicada

Explicada em:

- [tempo por status](../fatos/tempo-por-status.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqStatus` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idFrmStatus` | INT | não | não | não |
| `dtIniStatus` | DATETIME | não | não | não |
| `dtFimStatus` | DATETIME | sim | não | não |
| `nIntervaloReal` | INT | sim | não | não |
| `nIntervaloCal` | INT | sim | não | não |
| `dtUltimoAlerta` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqStatusConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
