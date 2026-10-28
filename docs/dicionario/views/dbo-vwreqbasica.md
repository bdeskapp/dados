---
gerado: sincronizacao
---

# dbo.vwReqBasica

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReq` | int |
| `ReqStatus` | varchar |
| `idFrm` | int |
| `nPrioridade` | tinyint |
| `dtAbertura` | datetime |
| `dtIniReal` | datetime |
| `dtIniPrev` | datetime |
| `dtFimReal` | datetime |
| `dtFimPrev` | datetime |
| `dsTitulo` | varchar |
| `idGru` | int |
| `idGruAtual` | int |
| `sla` | real |
| `idFrmStatus` | int |
| `dsSta` | varchar |
| `idHie` | int |
| `idFrmOrigem` | int |
| `idTar` | int |
| `VerbaPrevista` | money |
| `CustoTotal` | money |
| `tpReporteHora` | char |
| `idFlu` | int |
| `idProc` | int |
| `idRotina` | int |
| `tpControlaCusto` | char |
| `flgVIP` | bit |
| `idFluPai` | int |
| `idProcPai` | int |
| `idRotinaProcPai` | int |
| `flgReincidente` | bit |
| `nImp` | tinyint |
| `nUrg` | tinyint |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
