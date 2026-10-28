---
gerado: sincronizacao
---

# dbo.GrupoAcessoUsuario

**Selo:** Explicada

Explicada em:

- [grupo e área](../dimensoes/grupo-area.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtInicio` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.GrupoAcessoUsuario` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcessoUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcessoUsuario` (idGru) → `dbo.GrupoAcesso` (idGru)
