---
gerado: sincronizacao
---

# dbo.OsFluxo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlO` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |
| `idOS` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `dependenciaOSF` | VARCHAR(70) | sim | não | não |
| `flgSituacao` | TINYINT | não | não | não |
| `flgCriticidade` | TINYINT | não | não | não |
| `dtLiberacao` | SMALLDATETIME | sim | não | não |
| `sqOrdem` | INT | sim | não | não |
| `idFloTar` | INT | não | não | não |
| `DependenciaOSFAntiga` | VARCHAR(70) | sim | não | não |
| `idAre` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.OSFluxoProjeto` (idFlo, idTar) → `dbo.OsFluxo` (idFlO, idTar)
- `dbo.OsFluxo` (idAre) → `dbo.Area` (idAre)
- `dbo.OsFluxo` (idFlO) → `dbo.FluxoOS` (idFlO)
- `dbo.OsFluxo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OsFluxo` (idTar) → `dbo.Tarefa` (idTar)
