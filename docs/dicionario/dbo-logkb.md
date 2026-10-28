---
gerado: sincronizacao
---

# dbo.LogKB

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLog` | INT | não | sim | não |
| `idKB` | INT | não | não | não |
| `cdKBSta` | CHAR(3) | não | não | não |
| `dtLog` | DATETIME | não | não | não |
| `idUsu` | INT | não | não | não |
| `Estado` | TEXT | não | não | não |
| `idLogRef` | INT | sim | não | não |
| `dsObs` | VARCHAR(500) | sim | não | não |

## Chaves estrangeiras

- `dbo.LogKB` (idKB) → `dbo.KBase` (idKB)
- `dbo.LogKB` (idLogRef) → `dbo.LogKB` (idLog)
- `dbo.LogKB` (idUsu) → `dbo.Usuario` (idUsu)
