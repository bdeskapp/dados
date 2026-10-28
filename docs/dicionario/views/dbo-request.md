---
gerado: sincronizacao
---

# dbo.Request

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReq` | int |
| `idFrm` | int |
| `dsTitulo` | varchar |
| `dsReq` | text |
| `nPrioridade` | tinyint |
| `idFrmStatus` | int |
| `dsSta` | varchar |
| `idAre` | int |
| `dsAre` | varchar |
| `idCat` | int |
| `dsCat` | varchar |
| `idSca` | int |
| `dsSca` | varchar |
| `idTar` | int |
| `dsTar` | varchar |
| `dtAbertura` | datetime |
| `dtIniPrev` | datetime |
| `dtFimPrev` | datetime |
| `dtIniReal` | datetime |
| `dtFimReal` | datetime |
| `sla` | real |
| `slaReal` | real |
| `idGru` | int |
| `idFrmOrigem` | int |
| `dsFrmOrigem` | varchar |
| `idLoc` | int |
| `dsLoc` | varchar |
| `dsLocSistema` | varchar |
| `idPat` | int |
| `nmPat` | varchar |
| `numeroPat` | varchar |
| `seriePat` | varchar |
| `idHie` | int |
| `dsHie` | varchar |
| `idEmp` | int |
| `razaoSocial` | varchar |
| `flgForaSLA` | bit |
| `tpControlaCusto` | char |
| `tpControlaHora` | char |
| `TempoPrevisto` | real |
| `VerbaPrevista` | money |
| `TempoGastoTotal` | real |
| `CustoTotal` | money |
| `tpReporteHora` | char |
| `tpAgend` | tinyint |
| `idProc` | int |
| `idRotina` | int |
| `idFlu` | int |
| `difCustoVerba` | money |
| `flgVIP` | bit |
| `dtResposta` | datetime |
| `dtUltHistADO` | datetime |
| `SLAOrig` | real |
| `idGruAtual` | int |
| `idProcPai` | int |
| `idFluPai` | int |
| `idRotinaProcPai` | int |
| `nImp` | tinyint |
| `nUrg` | tinyint |
| `flgVinc` | bit |
| `flgDepende` | bit |
| `flgReincidente` | bit |
| `flgRecorrente` | bit |
| `flgN1Reg` | bit |
| `flgN1Conc` | bit |
| `tpAgenteReg` | char |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
