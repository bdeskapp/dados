---
gerado: sincronizacao
---

# dbo.ObjectSummaryDetail

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdObjSummary` | INT | não | sim | não |
| `cdObjQuery` | INT | não | sim | não |
| `nSeq` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.ObjectSummaryDetail` (cdObjQuery) → `dbo.ObjectQuery` (cdObj)
- `dbo.ObjectSummaryDetail` (cdObjSummary) → `dbo.ObjectSummary` (cdObj)
