---
gerado: sincronizacao
---

# dbo.OrgNivel

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNiv` | INT | não | sim | não |
| `cdNiv` | INT | não | não | não |
| `dsNiv` | VARCHAR(50) | não | não | não |
| `dtIniNiv` | DATETIME | não | não | não |
| `dtFimNiv` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.OrgHierarquia` (idNiv) → `dbo.OrgNivel` (idNiv)
