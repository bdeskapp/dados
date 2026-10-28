---
gerado: sincronizacao
---

# dbo.Imagem_Conteudo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Imagem_id` | BIGINT | não | sim | não |
| `Conteudo_id` | BIGINT | não | sim | não |

## Chaves estrangeiras

- `dbo.Imagem_Conteudo` (Conteudo_id) → `dbo.Conteudo` (Id)
- `dbo.Imagem_Conteudo` (Imagem_id) → `dbo.Imagem` (Id)
