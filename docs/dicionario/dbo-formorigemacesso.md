---
gerado: sincronizacao
---

# dbo.FormOrigemAcesso

**Selo:** Explicada

Explicada em:

- [canal e origem](../dimensoes/canal-origem.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmOrigem` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormOrigemAcesso` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.FormOrigemAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
