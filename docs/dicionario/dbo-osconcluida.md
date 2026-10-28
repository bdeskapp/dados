---
gerado: sincronizacao
---

# dbo.OSConcluida

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
| `nmUsu` | VARCHAR(100) | não | não | não |
| `flgVip` | BIT | não | não | não |
| `idCat` | INT | sim | não | não |
| `dsCat` | VARCHAR(30) | sim | não | não |
| `idSca` | INT | sim | não | não |
| `dsSca` | VARCHAR(30) | sim | não | não |
| `idTar` | INT | sim | não | não |
| `dsTar` | VARCHAR(40) | sim | não | não |
| `idGru` | INT | sim | não | não |
| `dsGru` | VARCHAR(50) | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `dsLoc` | VARCHAR(100) | sim | não | não |
| `idAvi` | INT | sim | não | não |
| `dsAvi` | VARCHAR(50) | sim | não | não |
| `idFlO` | INT | sim | não | não |
| `nmFlu` | VARCHAR(50) | sim | não | não |
| `idSta` | INT | não | não | não |
| `dsSta` | VARCHAR(15) | sim | não | não |
| `idTpco` | INT | sim | não | não |
| `dsTpco` | VARCHAR(30) | sim | não | não |
| `slaOS` | REAL | sim | não | não |
| `slaRealOS` | REAL | sim | não | não |
| `flgConfidencial` | BIT | não | não | não |
| `flgTpAgend` | TINYINT | sim | não | não |
| `flgMail` | BIT | não | não | não |
| `idUsuAbertura` | INT | sim | não | não |
| `nmUsuAbertura` | VARCHAR(100) | sim | não | não |
| `idUsuResponsavel` | INT | sim | não | não |
| `nmUsuResponsavel` | VARCHAR(100) | sim | não | não |
| `idPat` | INT | sim | não | não |
| `nmPat` | VARCHAR(30) | sim | não | não |
| `numero` | VARCHAR(30) | sim | não | não |
| `serie` | VARCHAR(20) | sim | não | não |
| `flgTpAbertura` | TINYINT | não | não | não |
| `estacao` | VARCHAR(20) | sim | não | não |
| `idEmp` | INT | sim | não | não |
| `RazaoSocial` | VARCHAR(50) | sim | não | não |
| `idHie` | INT | sim | não | não |
| `dsHie` | VARCHAR(100) | sim | não | não |
| `slaAtualOS` | REAL | sim | não | não |
| `ramal` | VARCHAR(5) | sim | não | não |
| `idGruAbertura` | INT | sim | não | não |
| `dsGruAbertura` | VARCHAR(50) | sim | não | não |
| `idTarAbertura` | INT | sim | não | não |
| `dsTarAbertura` | VARCHAR(40) | sim | não | não |
| `flgForaSLA` | TINYINT | sim | não | não |
| `flgTpReporteHora` | CHAR(1) | não | não | não |
| `TempoGastoTotal` | REAL | sim | não | não |
| `CustoTotal` | MONEY | sim | não | não |
| `dtFimPrevisto` | DATETIME | sim | não | não |
| `dtIniReal` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.OSAvaliacaoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
- `dbo.OSCustomConcluida` (idOs) → `dbo.OSConcluida` (idOs)
- `dbo.OSHistoricoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
- `dbo.OsAnexoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
