---
gerado: sincronizacao
---

# dbo.vwRepReqHistorico

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReqHist` | int |
| `idReq` | int |
| `NoReq` | int |
| `Situação` | varchar |
| `Formulário` | varchar |
| `Prioridade` | varchar |
| `Título` | varchar |
| `idFrmAcao` | int |
| `Ação` | varchar |
| `idMotivo` | int |
| `Data` | datetime |
| `Data Anterior` | datetime |
| `Intervalo` | int |
| `Descrição` | varchar |
| `idUsu` | int |
| `Usuário` | varchar |
| `idGru` | int |
| `idFrmStatus` | int |
| `Status` | varchar |
| `idFrm` | int |
| `idTar` | int |
| `idSca` | int |
| `Atividade Completa` | varchar |
| `Atividade` | varchar |
| `Subcategoria` | varchar |
| `Categoria` | varchar |
| `Tipo Atividade` | varchar |
| `idADO` | int |
| `Solicitado` | varchar |
| `Data Abertura` | datetime |
| `Data Fim` | datetime |
| `idReqPartAdo` | int |
| `idJus` | int |
| `idFlu` | int |
| `idProc` | int |
| `idRotina` | int |
| `idGruAbertura` | int |
| `idGruAtual` | int |
| `Area` | int |
| `idStatusReq` | int |
| `StatusReq` | varchar |
| `flgVip` | bit |
| `SLA` | real |
| `dtFimPrev` | datetime |
| `dtFimReal` | datetime |
| `idLoc` | int |
| `dsLoc` | varchar |
| `idImp` | int |
| `idUrg` | int |
| `nImp` | tinyint |
| `nUrg` | tinyint |
| `flgN1Reg` | bit |
| `flgN1Conc` | bit |
| `tpAgenteReg` | char |
| `idFluPai` | int |
| `idProcPai` | int |
| `idTpSla` | int |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
