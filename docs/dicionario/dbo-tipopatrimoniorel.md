---
gerado: sincronizacao
---

# dbo.TipoPatrimonioRel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpp` | INT | não | sim | não |
| `idTppRel` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.TipoPatrimonioRel` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.TipoPatrimonioRel` (idTppRel) → `dbo.TipoPatrimonio` (idTpp)
