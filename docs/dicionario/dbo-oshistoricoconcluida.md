---
gerado: sincronizacao
---

# dbo.OSHistoricoConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOS` | INT | não | sim | não |
| `dtIniOSH` | DATETIME | não | sim | não |
| `dtFimOSH` | DATETIME | sim | não | não |
| `idGru` | INT | não | não | não |
| `dsGru` | VARCHAR(50) | sim | não | não |
| `dsOSH` | TEXT | sim | não | não |
| `slaOSH` | REAL | sim | não | não |
| `idKB` | INT | sim | não | não |
| `nmKB` | VARCHAR(150) | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `nmUsu` | VARCHAR(100) | sim | não | não |
| `ValorHora` | MONEY | sim | não | não |
| `slaAtualOSH` | REAL | sim | não | não |
| `idCat` | INT | sim | não | não |
| `dsCat` | VARCHAR(30) | sim | não | não |
| `idSca` | INT | sim | não | não |
| `dsSca` | VARCHAR(30) | sim | não | não |
| `idTar` | INT | sim | não | não |
| `dsTar` | VARCHAR(40) | sim | não | não |
| `SLAOS` | REAL | sim | não | não |
| `idJus` | INT | sim | não | não |
| `dsJus` | VARCHAR(100) | sim | não | não |
| `idJusOSH` | INT | sim | não | não |
| `dsJusOSH` | VARCHAR(100) | sim | não | não |
| `TempoGasto` | REAL | sim | não | não |
| `flgConfidencial` | BIT | não | não | não |
| `idSta` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.OSHistoricoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
