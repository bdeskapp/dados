---
gerado: sincronizacao
---

# dbo.ReqApontAprov

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqApont` | INT | não | sim | não |
| `tpAprovacao` | CHAR(1) | sim | não | não |
| `dtInicio` | DATETIME | sim | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `qtdHoras` | SMALLINT | não | não | não |
| `dtAprovacao` | DATETIME | não | não | não |
| `idUsuAprov` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqApontAprov` (idReqApont) → `dbo.ReqApontamento` (idReqApont)
- `dbo.ReqApontAprov` (idUsuAprov) → `dbo.Usuario` (idUsu)
