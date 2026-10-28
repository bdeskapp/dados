---
gerado: sincronizacao
---

# dbo.Requisicao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Numero` | NVARCHAR(255) | não | não | não |
| `Solicitante` | NVARCHAR(255) | não | não | não |
| `CriadoEm` | DATETIME | não | não | não |
| `ItemCardapio_id` | BIGINT | não | não | não |
| `Sistema` | NVARCHAR(50) | não | não | não |
| `MetaDados` | XML | não | não | não |

## Chaves estrangeiras

- `dbo.Requisicao` (ItemCardapio_id) → `dbo.ItemCardapio` (Id)
