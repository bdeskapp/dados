---
gerado: sincronizacao
---

# dbo.Section

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdSection` | INT | não | sim | não |
| `nmSection` | NVARCHAR(30) | não | não | não |
| `nOrder` | TINYINT | não | não | não |
| `flgSummaryPage` | BIT | não | não | não |
| `cdObj` | INT | sim | não | não |
| `askKey` | NVARCHAR(50) | sim | não | não |

## Chaves estrangeiras

- `dbo.Item` (cdSection) → `dbo.Section` (cdSection)
- `dbo.Section` (cdObj) → `dbo.Object` (cdObj)
