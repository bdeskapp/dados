---
gerado: sincronizacao
---

# dbo.Object

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdObj` | INT | não | sim | não |
| `nmObj` | NVARCHAR(50) | não | não | não |
| `dsObj` | NVARCHAR(1000) | não | não | não |
| `tpObj` | CHAR(2) | não | não | não |
| `URLObj` | NVARCHAR(100) | sim | não | não |
| `askKey` | NVARCHAR(50) | sim | não | não |

## Chaves estrangeiras

- `dbo.Item` (cdObj) → `dbo.Object` (cdObj)
- `dbo.ObjectQuery` (cdObj) → `dbo.Object` (cdObj)
- `dbo.ObjectSummary` (cdObj) → `dbo.Object` (cdObj)
- `dbo.ProfileObject` (ObjectID) → `dbo.Object` (cdObj)
- `dbo.Section` (cdObj) → `dbo.Object` (cdObj)
