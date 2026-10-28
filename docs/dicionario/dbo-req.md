---
gerado: sincronizacao
---

# dbo.Req

**Selo:** Explicada

Explicada em:

- [canal e origem](../dimensoes/canal-origem.md)
- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)
- [prioridade e SLA](../dimensoes/prioridade-sla.md)
- [status](../dimensoes/status-fase.md)
- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)
- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)
- [marcos da requisição](../fatos/marcos.md)
- [requisição](../fatos/requisicao.md)
- [vínculos entre requisições](../fatos/vinculos.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `dsTitulo2` | VARCHAR(300) | sim | não | não |
| `dsReq` | VARCHAR(MAX) | não | não | não |
| `nPrioridade` | TINYINT | sim | não | não |
| `idFrmStatus` | INT | sim | não | não |
| `idAre` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `dtAbertura` | DATETIME | não | não | não |
| `dtIniPrev` | DATETIME | não | não | não |
| `dtFimPrev` | DATETIME | não | não | não |
| `dtIniReal` | DATETIME | sim | não | não |
| `dtFimReal` | DATETIME | sim | não | não |
| `sla` | REAL | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `dsLoc` | VARCHAR(100) | sim | não | não |
| `idPat` | INT | sim | não | não |
| `idHie` | INT | sim | não | não |
| `idEmp` | INT | sim | não | não |
| `flgForaSLA` | BIT | não | não | não |
| `tpControlaCusto` | CHAR(1) | não | não | não |
| `tpControlaHora` | CHAR(1) | não | não | não |
| `TempoPrevisto` | REAL | sim | não | não |
| `VerbaPrevista` | MONEY | sim | não | não |
| `TempoGastoTotal` | REAL | sim | não | não |
| `CustoTotal` | MONEY | sim | não | não |
| `tpReporteHora` | CHAR(1) | sim | não | não |
| `tpAgend` | TINYINT | sim | não | não |
| `idProc` | INT | sim | não | não |
| `idRotina` | INT | sim | não | não |
| `idFlu` | INT | sim | não | não |
| `difCustoVerba` | computada | sim | não | sim |
| `flgVIP` | BIT | não | não | não |
| `dtResposta` | DATETIME | sim | não | não |
| `dtUltHistADO` | DATETIME | sim | não | não |
| `SLAOrig` | REAL | sim | não | não |
| `idGruAtual` | INT | sim | não | não |
| `idProcPai` | INT | sim | não | não |
| `idFluPai` | INT | sim | não | não |
| `idRotinaProcPai` | INT | sim | não | não |
| `nImp` | TINYINT | sim | não | não |
| `nUrg` | TINYINT | sim | não | não |
| `flgVinc` | BIT | sim | não | não |
| `flgDepende` | BIT | sim | não | não |
| `flgReincidente` | BIT | não | não | não |
| `flgRecorrente` | BIT | não | não | não |
| `flgN1Reg` | BIT | não | não | não |
| `flgN1Conc` | BIT | não | não | não |
| `tpAgenteReg` | CHAR(1) | sim | não | não |
| `idItemCardapio` | BIGINT | sim | não | não |
| `dsTitulo` | VARCHAR(500) | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.LicReserva` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqAprov` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqDespesa` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqDocumento` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqHistorico` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqKB` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMensagem` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMinutaHistorico` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMinuta` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqParticipante` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqPendencia` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqPlanoAlerta` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqProblema` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqStatus` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqTimeAdo` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqTimeout` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqTime` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqTransTimeout` (idReq) → `dbo.Req` (idReq)
- `dbo.Req` (idAre) → `dbo.Area` (idAre)
- `dbo.Req` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.Req` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.Req` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Req` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Req` (idGru) → `dbo.Grupo` (idGru)
- `dbo.Req` (idItemCardapio) → `dbo.ItemCardapio` (Id)
- `dbo.Req` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Req` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.Req` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.Req` (idProc) → `dbo.Processo` (idProc)
- `dbo.Req` (idProcPai) → `dbo.Processo` (idProc)
- `dbo.Req` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Req` (idRotinaProcPai) → `dbo.Rotina` (idRotina)
- `dbo.Req` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.Req` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Req` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.Req` (idFluPai) → `dbo.Workflow` (idFlu)
