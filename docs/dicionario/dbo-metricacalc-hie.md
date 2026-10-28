---
gerado: sincronizacao
---

# dbo.MetricaCalc_Hie

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCalcHie` | INT | não | sim | não |
| `cdMetrica` | INT | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtRef` | DATETIME | não | não | não |
| `idHie` | INT | não | não | não |
| `idAre` | INT | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `valCalc` | INT | não | não | não |
| `dtCalc` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_Hie` (idAre) → `dbo.Area` (idAre)
- `dbo.MetricaCalc_Hie` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Hie` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Hie` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.MetricaCalc_Hie` (idTar) → `dbo.Tarefa` (idTar)
