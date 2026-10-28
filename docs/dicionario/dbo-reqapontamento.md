---
gerado: sincronizacao
---

# dbo.ReqApontamento

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)

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
| `dtBase` | SMALLDATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.ReqApontAprov` (idReqApont) → `dbo.ReqApontamento` (idReqApont)
