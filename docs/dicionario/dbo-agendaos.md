---
gerado: sincronizacao
---

# dbo.AgendaOS

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `IdAge` | INT | não | sim | não |
| `IdUsu` | INT | não | não | não |
| `IdTar` | INT | não | não | não |
| `IdGru` | INT | não | não | não |
| `flgConfidencial` | BIT | não | não | não |
| `dsOs` | TEXT | sim | não | não |
| `dtInicial` | DATETIME | não | não | não |
| `dtFinal` | DATETIME | sim | não | não |
| `flgRecorrencia` | CHAR(1) | não | não | não |
| `flgUltDiaMes` | BIT | não | não | não |
| `Antecedencia` | SMALLINT | não | não | não |
| `flgTipoAntecedencia` | CHAR(1) | não | não | não |
| `dtUltExecucao` | DATETIME | sim | não | não |
| `UltOsAberta` | INT | sim | não | não |
| `idUsuCriador` | INT | não | não | não |
| `dtCriacao` | DATETIME | não | não | não |
| `flgAgeAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaOSCustom` (idAge) → `dbo.AgendaOS` (IdAge)
- `dbo.AgendaOS` (IdGru) → `dbo.Grupo` (idGru)
- `dbo.AgendaOS` (IdTar) → `dbo.Tarefa` (idTar)
