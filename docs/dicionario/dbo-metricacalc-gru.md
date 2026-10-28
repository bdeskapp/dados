---
gerado: sincronizacao
---

# dbo.MetricaCalc_Gru

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCalcGru` | INT | não | sim | não |
| `cdMetrica` | INT | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtRef` | DATETIME | não | não | não |
| `idGru` | INT | não | não | não |
| `idFrm` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `valCalc` | INT | não | não | não |
| `dtCalc` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_Gru` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Gru` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MetricaCalc_Gru` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Gru` (idTar) → `dbo.Tarefa` (idTar)
