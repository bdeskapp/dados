---
gerado: sincronizacao
---

# dbo.ReqTimeAdo

**Selo:** Explicada

Explicada em:

- [tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

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

- `dbo.ReqTimeAdo` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqTimeAdo` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
