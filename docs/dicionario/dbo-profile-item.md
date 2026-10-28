---
gerado: sincronizacao
---

# dbo.Profile_Item

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idProfile` | INT | não | não | não |
| `idItem` | INT | não | sim | não |
| `flgRW` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Profile_Item` (idItem) → `dbo.Item` (idItem)
- `dbo.Profile_Item` (idProfile) → `dbo.Perfil` (idPer)
