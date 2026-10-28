---
gerado: sincronizacao
---

# dbo.ProfileObject

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `ProfileID` | INT | não | sim | não |
| `ObjectID` | INT | não | sim | não |
| `AccessType` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.ProfileObject` (ObjectID) → `dbo.Object` (cdObj)
- `dbo.ProfileObject` (ProfileID) → `dbo.Perfil` (idPer)
