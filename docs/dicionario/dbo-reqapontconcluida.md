---
gerado: sincronizacao
---

# dbo.ReqApontConcluida

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqApont` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtInicio` | DATETIME | sim | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `qtdHoras` | SMALLINT | não | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `idUsuReporte` | INT | não | não | não |
| `idSeq` | INT | não | não | não |
| `dtBase` | SMALLDATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqApontAprovConcluida` (idReqApont) → `dbo.ReqApontConcluida` (idReqApont)
