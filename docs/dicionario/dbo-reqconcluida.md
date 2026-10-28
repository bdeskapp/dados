---
gerado: sincronizacao
---

# dbo.ReqConcluida

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
| `idFrmStatus` | INT | não | não | não |
| `dsSta` | VARCHAR(30) | não | não | não |
| `idAre` | INT | sim | não | não |
| `dsAre` | VARCHAR(100) | sim | não | não |
| `idCat` | INT | sim | não | não |
| `dsCat` | VARCHAR(100) | sim | não | não |
| `idSca` | INT | sim | não | não |
| `dsSca` | VARCHAR(100) | sim | não | não |
| `idTar` | INT | sim | não | não |
| `dsTar` | VARCHAR(100) | sim | não | não |
| `dtAbertura` | DATETIME | não | não | não |
| `dtIniPrev` | DATETIME | não | não | não |
| `dtFimPrev` | DATETIME | não | não | não |
| `dtIniReal` | DATETIME | sim | não | não |
| `dtFimReal` | DATETIME | sim | não | não |
| `Sla` | REAL | sim | não | não |
| `SlaReal` | REAL | sim | não | não |
| `idGru` | INT | sim | não | não |
| `dsGru` | VARCHAR(50) | sim | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `dsFrmOrigem` | VARCHAR(30) | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `dsLocSistema` | VARCHAR(100) | sim | não | não |
| `dsLoc` | VARCHAR(100) | sim | não | não |
| `idPat` | INT | sim | não | não |
| `nmPat` | VARCHAR(100) | sim | não | não |
| `numeroPat` | VARCHAR(30) | sim | não | não |
| `seriePat` | VARCHAR(100) | sim | não | não |
| `idHie` | INT | sim | não | não |
| `dsHie` | VARCHAR(100) | sim | não | não |
| `idEmp` | INT | sim | não | não |
| `RazaoSocial` | VARCHAR(50) | sim | não | não |
| `flgForaSla` | BIT | não | não | não |
| `tpControlaCusto` | CHAR(1) | não | não | não |
| `tpControlaHora` | CHAR(1) | não | não | não |
| `TempoPrevisto` | REAL | sim | não | não |
| `VerbaPrevista` | MONEY | sim | não | não |
| `TempoGastoTotal` | REAL | sim | não | não |
| `CustoTotal` | MONEY | sim | não | não |
| `tpReporteHora` | CHAR(1) | sim | não | não |
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
| `flgReincidente` | BIT | não | não | não |
| `flgRecorrente` | BIT | não | não | não |
| `flgN1Reg` | BIT | não | não | não |
| `flgN1Conc` | BIT | não | não | não |
| `tpAgenteReg` | CHAR(1) | sim | não | não |
| `flgDepende` | BIT | sim | não | não |
| `idItemCardapio` | BIGINT | sim | não | não |
| `dsTitulo` | VARCHAR(500) | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqConcluida` (idItemCardapio) → `dbo.ItemCardapio` (Id)
- `dbo.ReqConcluida` (idProc) → `dbo.Processo` (idProc)
- `dbo.ReqConcluida` (idProcPai) → `dbo.Processo` (idProc)
- `dbo.ReqConcluida` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ReqConcluida` (idRotinaProcPai) → `dbo.Rotina` (idRotina)
- `dbo.ReqConcluida` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqConcluida` (idFluPai) → `dbo.Workflow` (idFlu)
- `dbo.ReqDespConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqDocConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqHistConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqKBConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqMinutaConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqMinutaHistConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqMsgConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqPartConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqPendConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqProblemaConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqStatusConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqTimeAdoConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqTimeConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
