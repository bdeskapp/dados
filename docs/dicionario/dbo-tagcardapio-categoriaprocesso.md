---
gerado: sincronizacao
---

# dbo.TagCardapio_CategoriaProcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTag` | INT | não | sim | não |
| `idCatProc` | SMALLINT | não | sim | não |

## Chaves estrangeiras

- `dbo.TagCardapio_CategoriaProcesso` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.TagCardapio_CategoriaProcesso` (idTag) → `dbo.TagCardapio` (idTag)
