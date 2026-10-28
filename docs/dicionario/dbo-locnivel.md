---
gerado: sincronizacao
---

# dbo.LocNivel

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLocNiv` | INT | não | sim | não |
| `cdLoc` | INT | não | não | não |
| `dsLocNiv` | VARCHAR(50) | não | não | não |
| `dtIniLoc` | DATETIME | não | não | não |
| `dtFimLoc` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.Localiza` (idLocNiv) → `dbo.LocNivel` (idLocNiv)
