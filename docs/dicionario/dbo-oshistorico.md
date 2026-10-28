---
gerado: sincronizacao
---

# dbo.OSHistorico

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
| `dsOSH` | TEXT | sim | não | não |
| `slaOSH` | REAL | sim | não | não |
| `idKB` | INT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `ValorHora` | MONEY | sim | não | não |
| `slaAtualOSH` | REAL | sim | não | não |
| `idTar` | INT | sim | não | não |
| `SLAOS` | REAL | sim | não | não |
| `idJus` | INT | sim | não | não |
| `idJusOSH` | INT | sim | não | não |
| `TempoGasto` | REAL | sim | não | não |
| `flgConfidencial` | BIT | não | não | não |
| `idSta` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.OSHistorico` (idJus) → `dbo.Justificativa` (idJus)
- `dbo.OSHistorico` (idJusOSH) → `dbo.Justificativa` (idJus)
- `dbo.OSHistorico` (idOS) → `dbo.OS` (idOs)
- `dbo.OSHistorico` (idTar) → `dbo.Tarefa` (idTar)
