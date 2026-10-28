---
gerado: sincronizacao
---

# dbo.Item

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idItem` | INT | não | sim | não |
| `nmItem` | NVARCHAR(50) | não | não | não |
| `cdSection` | INT | não | não | não |
| `cdObj` | INT | sim | não | não |
| `idParent` | INT | sim | não | não |
| `obsItem` | NVARCHAR(MAX) | sim | não | não |

## Chaves estrangeiras

- `dbo.Item` (idParent) → `dbo.Item` (idItem)
- `dbo.Item` (cdObj) → `dbo.Object` (cdObj)
- `dbo.Item` (cdSection) → `dbo.Section` (cdSection)
- `dbo.Profile_Item` (idItem) → `dbo.Item` (idItem)
