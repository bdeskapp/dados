---
gerado: sincronizacao
---

# dbo.GrupoAcesso_ItemCardapio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idIc` | BIGINT | não | sim | não |

## Chaves estrangeiras

- `dbo.GrupoAcesso_ItemCardapio` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcesso_ItemCardapio` (idIc) → `dbo.ItemCardapio` (Id)
