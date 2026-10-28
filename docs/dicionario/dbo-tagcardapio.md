---
gerado: sincronizacao
---

# dbo.TagCardapio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTag` | INT | não | sim | não |
| `dsTag` | VARCHAR(255) | não | não | não |
| `imagem` | VARCHAR(255) | não | não | não |
| `flgDestacar` | BIT | não | não | não |
| `nPeso` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.TagCardapio_CategoriaProcesso` (idTag) → `dbo.TagCardapio` (idTag)
- `dbo.TagCardapio_Categoria_ItemCardapio` (idTag) → `dbo.TagCardapio` (idTag)
