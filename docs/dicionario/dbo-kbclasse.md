---
gerado: sincronizacao
---

# dbo.KBClasse

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAre` | INT | não | sim | não |
| `cdKBClas` | CHAR(3) | não | sim | não |
| `dsKBClas` | VARCHAR(30) | não | não | não |
| `tpAprov` | TINYINT | não | não | não |
| `idGruAprov` | INT | sim | não | não |
| `tpAcesso` | TINYINT | não | não | não |
| `tpAvalia` | TINYINT | não | não | não |
| `idGruAvalia` | INT | sim | não | não |
| `flgNotContrib` | BIT | não | não | não |
| `idMas` | INT | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.KBClasse` (idAre) → `dbo.Area` (idAre)
- `dbo.KBClasse` (idGruAprov) → `dbo.Grupo` (idGru)
- `dbo.KBClasse` (idGruAvalia) → `dbo.Grupo` (idGru)
- `dbo.KBClasse` (idMas) → `dbo.Mascara` (idMascara)
- `dbo.KBStatus` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.KBase` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.MetricaCalc_KBUtil` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.MetricaCalc_KB` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
