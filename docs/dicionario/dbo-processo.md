---
gerado: sincronizacao
---

# dbo.Processo

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idProc` | INT | não | sim | não |
| `cdProc` | INT | não | não | não |
| `vsProc` | TINYINT | não | não | não |
| `dsProc` | VARCHAR(50) | não | não | não |
| `idGruAdm` | INT | não | não | não |
| `obsProc` | TEXT | sim | não | não |
| `idUsuAutor` | INT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idAre` | INT | sim | não | não |
| `idCatProc` | SMALLINT | sim | não | não |
| `dsProcComp` | VARCHAR(100) | sim | não | não |
| `tpAut` | CHAR(1) | não | não | não |
| `idFrmAut` | INT | sim | não | não |
| `idUsuRevisor` | INT | sim | não | não |
| `dtAlteracao` | DATETIME | sim | não | não |
| `dtValidacao` | DATETIME | sim | não | não |
| `qtdErros` | SMALLINT | sim | não | não |
| `qtdAlertas` | SMALLINT | sim | não | não |
| `qtdRecomenda` | SMALLINT | sim | não | não |
| `flgPlan` | BIT | não | não | não |
| `nPrazo` | INT | sim | não | não |
| `tpCalcPrazo` | CHAR(1) | sim | não | não |
| `flgAtivo` | BIT | não | não | não |
| `flgHistFluxo` | BIT | não | não | não |
| `flgTemplate` | BIT | não | não | não |
| `flgAtivFluxo` | BIT | não | não | não |
| `flgReplicaPrazoEtapa` | BIT | sim | não | não |
| `flgVisualizarVincEtapa` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReq` (idProc) → `dbo.Processo` (idProc)
- `dbo.Condicao` (idProc) → `dbo.Processo` (idProc)
- `dbo.LicConfig` (idProc) → `dbo.Processo` (idProc)
- `dbo.ProcessoRegraPlan` (idProc) → `dbo.Processo` (idProc)
- `dbo.ProcessoValida` (idProc) → `dbo.Processo` (idProc)
- `dbo.Processo` (idAre) → `dbo.Area` (idAre)
- `dbo.Processo` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.Processo` (idFrmAut) → `dbo.Formulario` (idFrm)
- `dbo.Processo` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.Processo` (idUsuAutor) → `dbo.Usuario` (idUsu)
- `dbo.Processo` (idUsuRevisor) → `dbo.Usuario` (idUsu)
- `dbo.ReqConcluida` (idProc) → `dbo.Processo` (idProc)
- `dbo.ReqConcluida` (idProcPai) → `dbo.Processo` (idProc)
- `dbo.Req` (idProc) → `dbo.Processo` (idProc)
- `dbo.Req` (idProcPai) → `dbo.Processo` (idProc)
- `dbo.Rotina` (idProc) → `dbo.Processo` (idProc)
- `dbo.Rotina` (idProcSub) → `dbo.Processo` (idProc)
- `dbo.Workflow` (idProc) → `dbo.Processo` (idProc)
