---
gerado: sincronizacao
---

# dbo.MetricaRef

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdRef` | VARCHAR(6) | não | sim | não |
| `dsRef` | VARCHAR(50) | não | não | não |
| `nmTable` | VARCHAR(50) | sim | não | não |

## Chaves estrangeiras

- `dbo.Metrica` (cdRef) → `dbo.MetricaRef` (cdRef)
