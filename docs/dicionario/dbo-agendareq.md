---
gerado: sincronizacao
---

# dbo.AgendaReq

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAge` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `dsTitulo` | VARCHAR(100) | não | não | não |
| `dsReq` | TEXT | não | não | não |
| `nPrioridade` | TINYINT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `dsLoc` | VARCHAR(100) | sim | não | não |
| `VerbaPrevista` | MONEY | sim | não | não |
| `dtInicial` | DATETIME | não | não | não |
| `dtFinal` | DATETIME | sim | não | não |
| `tpRecorrencia` | CHAR(1) | não | não | não |
| `nDiasRecorrencia` | SMALLINT | sim | não | não |
| `tpAntecedencia` | CHAR(1) | não | não | não |
| `nAntecedencia` | SMALLINT | não | não | não |
| `idUsuResponsavel` | INT | não | não | não |
| `idGruResponsavel` | INT | não | não | não |
| `dtAtualizacao` | DATETIME | não | não | não |
| `flgHabilitado` | BIT | não | não | não |
| `dtUltExecucao` | DATETIME | sim | não | não |
| `idReqUltima` | INT | sim | não | não |
| `flgUltDiaMes` | BIT | não | não | não |
| `flgUltDiaUtil` | BIT | não | não | não |
| `flgAntecipar` | BIT | não | não | não |
| `flgDtFim` | BIT | não | não | não |
| `dtUltExecucaoReal` | DATETIME | sim | não | não |
| `idProc` | INT | sim | não | não |
| `idRotina` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.AgendaReqPart` (idAge) → `dbo.AgendaReq` (idAge)
- `dbo.AgendaReq` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.AgendaReq` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.AgendaReq` (idGruResponsavel) → `dbo.Grupo` (idGru)
- `dbo.AgendaReq` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.AgendaReq` (idProc) → `dbo.Processo` (idProc)
- `dbo.AgendaReq` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.AgendaReq` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.AgendaReq` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Contrato` (idAgeRenov) → `dbo.AgendaReq` (idAge)
