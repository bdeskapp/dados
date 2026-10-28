---
gerado: sincronizacao
---

# dbo.ConteudoCategoria

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [base de conhecimento](../fora-de-escopo/base-de-conhecimento.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Descricao` | NVARCHAR(255) | sim | não | não |
| `Slug` | NVARCHAR(255) | não | não | não |
| `Nome` | NVARCHAR(255) | não | não | não |
| `NomeCompleto` | NVARCHAR(255) | sim | não | não |
| `Peso` | INT | sim | não | não |
| `CategoriaPai_id` | BIGINT | sim | não | não |
| `TotalConteudos` | BIGINT | sim | não | não |
| `GruposAcesso` | NVARCHAR(255) | não | não | não |

## Chaves estrangeiras

- `dbo.ConteudoCategoria` (CategoriaPai_id) → `dbo.ConteudoCategoria` (Id)
- `dbo.Conteudo` (Categoria_id) → `dbo.ConteudoCategoria` (Id)
