---
gerado: sincronizacao
---

# dbo.MetricaCalc_Ger

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCalcGer` | INT | não | sim | não |
| `cdMetrica` | INT | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtRef` | DATETIME | não | não | não |
| `valCalc` | INT | não | não | não |
| `dtCalc` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_Ger` (cdMetrica) → `dbo.Metrica` (cdMetrica)
