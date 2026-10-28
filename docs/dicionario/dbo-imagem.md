---
gerado: sincronizacao
---

# dbo.Imagem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Titulo` | NVARCHAR(255) | sim | não | não |
| `Descricao` | NVARCHAR(255) | sim | não | não |
| `Caminho` | NVARCHAR(255) | sim | não | não |

## Chaves estrangeiras

- `dbo.Imagem_Conteudo` (Imagem_id) → `dbo.Imagem` (Id)
