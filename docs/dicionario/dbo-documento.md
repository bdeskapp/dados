---
gerado: sincronizacao
---

# dbo.Documento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Nome` | NVARCHAR(255) | não | não | não |
| `Url` | NVARCHAR(255) | não | não | não |

## Chaves estrangeiras

- `dbo.Anexo` (Documento_Id) → `dbo.Documento` (Id)
- `dbo.Conteudo` (Documento_Id) → `dbo.Documento` (Id)
