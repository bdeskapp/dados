---
gerado: sincronizacao
---

# dbo.GrupoAcessoTipoPapel

**Selo:** Explicada

Explicada em:

- [grupo e área](../dimensoes/grupo-area.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `dtInicio` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.GrupoAcessoTipoPapel` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoTipoPapel` (idUsuOperacao) → `dbo.Usuario` (idUsu)
