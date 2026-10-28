---
gerado: sincronizacao
---

# dbo.UsuarioCategoria_ItemCardapio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `id` | INT | não | sim | não |
| `idUsu` | INT | não | não | não |
| `idCic` | BIGINT | não | não | não |
| `idCatProc` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.UsuarioCategoria_ItemCardapio` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.UsuarioCategoria_ItemCardapio` (idCic) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.UsuarioCategoria_ItemCardapio` (idUsu) → `dbo.Usuario` (idUsu)
