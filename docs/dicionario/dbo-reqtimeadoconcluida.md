---
gerado: sincronizacao
---

# dbo.ReqTimeAdoConcluida

**Selo:** Explicada

Explicada em:

- [tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqPart` | INT | não | sim | não |
| `dtCalc` | DATETIME | não | não | não |
| `tAtivo` | INT | sim | não | não |
| `tFreeze` | INT | sim | não | não |
| `tAtivoCal` | INT | sim | não | não |
| `tFreezeCal` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqTimeAdoConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqTimeAdoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
