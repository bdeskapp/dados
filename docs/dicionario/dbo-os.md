---
gerado: sincronizacao
---

# dbo.OS

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOs` | INT | não | sim | não |
| `dtAbertura` | DATETIME | não | não | não |
| `dtIniOS` | DATETIME | não | não | não |
| `dtFimOS` | DATETIME | sim | não | não |
| `dtFimAgend` | DATETIME | sim | não | não |
| `dsOS` | TEXT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `idTar` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `idAvi` | INT | sim | não | não |
| `idFlO` | INT | sim | não | não |
| `idSta` | INT | não | não | não |
| `idTpco` | INT | sim | não | não |
| `slaOS` | REAL | sim | não | não |
| `slaRealOS` | REAL | sim | não | não |
| `flgConfidencial` | BIT | não | não | não |
| `flgTpAgend` | TINYINT | sim | não | não |
| `flgMail` | BIT | não | não | não |
| `idUsuAbertura` | INT | sim | não | não |
| `idUsuResponsavel` | INT | sim | não | não |
| `idPat` | INT | sim | não | não |
| `flgTpAbertura` | TINYINT | não | não | não |
| `estacao` | VARCHAR(20) | sim | não | não |
| `idEmp` | INT | sim | não | não |
| `idhie` | INT | sim | não | não |
| `slaAtualOS` | REAL | sim | não | não |
| `idTarAbertura` | INT | sim | não | não |
| `idGruAbertura` | INT | sim | não | não |
| `flgForaSLA` | TINYINT | sim | não | não |
| `flgUltOSMultipla` | TINYINT | sim | não | não |
| `flgOSMultipla` | TINYINT | sim | não | não |
| `flgTpReporteHora` | CHAR(1) | não | não | não |
| `TempoGastoTotal` | REAL | sim | não | não |
| `CustoTotal` | MONEY | sim | não | não |
| `dtFimPrevisto` | DATETIME | sim | não | não |
| `dtIniReal` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.OSAvaliacao` (idOS) → `dbo.OS` (idOs)
- `dbo.OSCustom` (idOs) → `dbo.OS` (idOs)
- `dbo.OSHistorico` (idOS) → `dbo.OS` (idOs)
- `dbo.OSPlanoAlerta` (idOS) → `dbo.OS` (idOs)
- `dbo.OS` (idAvi) → `dbo.Aviso` (idAvi)
- `dbo.OS` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.OS` (idFlO) → `dbo.FluxoOS` (idFlO)
- `dbo.OS` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OS` (idGruAbertura) → `dbo.Grupo` (idGru)
- `dbo.OS` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.OS` (idhie) → `dbo.OrgHierarquia` (idHie)
- `dbo.OS` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.OS` (idSta) → `dbo.Status` (idSta)
- `dbo.OS` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.OS` (idTarAbertura) → `dbo.Tarefa` (idTar)
- `dbo.OS` (idTpco) → `dbo.TipoConclusao` (idTpco)
- `dbo.OS` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.OS` (idUsuAbertura) → `dbo.Usuario` (idUsu)
- `dbo.OS` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.OsAnexo` (idOS) → `dbo.OS` (idOs)
