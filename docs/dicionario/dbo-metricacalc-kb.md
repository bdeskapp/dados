---
gerado: sincronizacao
---

# dbo.MetricaCalc_KB

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCalcKB` | INT | não | sim | não |
| `cdMetrica` | INT | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtRef` | DATETIME | não | não | não |
| `idAre` | INT | não | não | não |
| `cdKBClas` | CHAR(3) | não | não | não |
| `idGru` | INT | não | não | não |
| `valCalc` | INT | não | não | não |
| `dtCalc` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_KB` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MetricaCalc_KB` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.MetricaCalc_KB` (cdMetrica) → `dbo.Metrica` (cdMetrica)
