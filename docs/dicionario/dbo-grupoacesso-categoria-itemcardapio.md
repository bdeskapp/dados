---
gerado: sincronizacao
---

# dbo.GrupoAcesso_Categoria_ItemCardapio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idCic` | BIGINT | não | sim | não |

## Chaves estrangeiras

- `dbo.GrupoAcesso_Categoria_ItemCardapio` (idCic) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.GrupoAcesso_Categoria_ItemCardapio` (idGru) → `dbo.GrupoAcesso` (idGru)
