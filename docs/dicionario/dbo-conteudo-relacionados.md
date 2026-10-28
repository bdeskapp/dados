---
gerado: sincronizacao
---

# dbo.Conteudo_Relacionados

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Conteudo_id` | BIGINT | não | sim | não |
| `ConteudoRelacionado_id` | BIGINT | não | sim | não |

## Chaves estrangeiras

- `dbo.Conteudo_Relacionados` (Conteudo_id) → `dbo.Conteudo` (Id)
- `dbo.Conteudo_Relacionados` (ConteudoRelacionado_id) → `dbo.Conteudo` (Id)
