---
gerado: sincronizacao
---

# dbo.Anexo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Documento_Id` | BIGINT | não | não | não |
| `Index` | UNIQUEIDENTIFIER | não | sim | não |
| `Extensao` | VARCHAR(225) | sim | não | não |
| `Tamanho` | INT | não | não | não |
| `Anexo` | VARBINARY(MAX) | não | não | não |

## Chaves estrangeiras

- `dbo.Anexo` (Documento_Id) → `dbo.Documento` (Id)
