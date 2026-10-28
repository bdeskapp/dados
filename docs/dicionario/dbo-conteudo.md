---
gerado: sincronizacao
---

# dbo.Conteudo

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [base de conhecimento](../fora-de-escopo/base-de-conhecimento.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Titulo` | NVARCHAR(255) | não | não | não |
| `Resumo` | NVARCHAR(150) | não | não | não |
| `Corpo` | NTEXT | sim | não | não |
| `EhFaq` | BIT | sim | não | não |
| `Peso` | INT | sim | não | não |
| `Ativo` | BIT | sim | não | não |
| `Categoria_id` | BIGINT | não | não | não |
| `Likes` | INT | sim | não | não |
| `PageViews` | INT | sim | não | não |
| `UnLikes` | INT | sim | não | não |
| `GruposAcesso` | NVARCHAR(255) | não | não | não |
| `Tipo` | NVARCHAR(255) | não | não | não |
| `Documento_Id` | BIGINT | sim | não | não |
| `Slug` | NVARCHAR(255) | sim | não | não |
| `CorpoTextoPlano` | NTEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.Conteudo_Relacionados` (Conteudo_id) → `dbo.Conteudo` (Id)
- `dbo.Conteudo_Relacionados` (ConteudoRelacionado_id) → `dbo.Conteudo` (Id)
- `dbo.Conteudo` (Categoria_id) → `dbo.ConteudoCategoria` (Id)
- `dbo.Conteudo` (Documento_Id) → `dbo.Documento` (Id)
- `dbo.Imagem_Conteudo` (Conteudo_id) → `dbo.Conteudo` (Id)
- `dbo.Tag_Conteudo` (Conteudo_id) → `dbo.Conteudo` (Id)
