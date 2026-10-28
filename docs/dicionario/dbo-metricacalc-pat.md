---
gerado: sincronizacao
---

# dbo.MetricaCalc_Pat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCalcPat` | INT | não | sim | não |
| `cdMetrica` | INT | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtRef` | DATETIME | não | não | não |
| `idTpp` | INT | não | não | não |
| `idLoc` | INT | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `valCalc` | INT | não | não | não |
| `dtCalc` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_Pat` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Pat` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.MetricaCalc_Pat` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Pat` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.MetricaCalc_Pat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
