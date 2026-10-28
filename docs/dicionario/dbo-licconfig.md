---
gerado: sincronizacao
---

# dbo.LicConfig

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGruAdm` | INT | sim | não | não |
| `flgControleAtivo` | BIT | não | não | não |
| `flgAgendaAtualizacao` | BIT | não | não | não |
| `dtAgendaAtualizacao` | DATETIME | sim | não | não |
| `dtAtualizacao` | DATETIME | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `idUsuSolicitante` | INT | sim | não | não |
| `idProc` | INT | sim | não | não |
| `idFrmOrigem` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.LicConfig` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.LicConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.LicConfig` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.LicConfig` (idProc) → `dbo.Processo` (idProc)
- `dbo.LicConfig` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.LicConfig` (idUsuSolicitante) → `dbo.Usuario` (idUsu)
