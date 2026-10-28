---
gerado: sincronizacao
---

# dbo.Categoria_ItemCardapio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Nome` | NVARCHAR(255) | não | não | não |
| `Imagem` | NVARCHAR(255) | não | não | não |
| `GruposAcesso` | NVARCHAR(255) | não | não | não |
| `Ativo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.GrupoAcesso_Categoria_ItemCardapio` (idCic) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.ItemCardapio` (Categoria_ItemCardapio_id) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.TagCardapio_Categoria_ItemCardapio` (idCic) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.UsuarioCategoria_ItemCardapio` (idCic) → `dbo.Categoria_ItemCardapio` (Id)
