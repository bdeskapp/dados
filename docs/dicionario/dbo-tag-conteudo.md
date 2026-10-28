---
gerado: sincronizacao
---

# dbo.Tag_Conteudo

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [base de conhecimento](../fora-de-escopo/base-de-conhecimento.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Conteudo_id` | BIGINT | não | sim | não |
| `Tag_id` | BIGINT | não | sim | não |

## Chaves estrangeiras

- `dbo.Tag_Conteudo` (Conteudo_id) → `dbo.Conteudo` (Id)
- `dbo.Tag_Conteudo` (Tag_id) → `dbo.Tag` (Id)
