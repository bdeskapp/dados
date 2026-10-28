---
gerado: sincronizacao
---

# dbo.vwRepReq

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReq` | int |
| `NoReq` | int |
| `Situação` | varchar |
| `Formulário` | varchar |
| `Prioridade` | varchar |
| `Data de Abertura` | datetime |
| `Data de Início Real` | datetime |
| `Data de Início Prevista` | datetime |
| `Data de Término Real` | datetime |
| `Data de Término Prevista` | datetime |
| `Data de Resposta` | datetime |
| `Título` | varchar |
| `idGru` | int |
| `SLA` | real |
| `idFrmStatus` | int |
| `Status` | varchar |
| `Registrador` | varchar |
| `Solicitante` | varchar |
| `Solicitado` | varchar |
| `Responsável` | varchar |
| `Beneficiado` | varchar |
| `Atividade Completa` | varchar |
| `Atividade` | varchar |
| `Subcategoria` | varchar |
| `Categoria` | varchar |
| `idTar` | int |
| `idSca` | int |
| `Verba` | money |
| `Custo` | money |
| `Saldo` | money |
| `Descrição` | int |
| `idFrmOrigem` | int |
| `idLoc` | int |
| `dsLoc` | varchar |
| `tpAgend` | int |
| `flgVip` | bit |
| `idFrm` | int |
| `idGruAtual` | int |
| `idFlu` | int |
| `idRotina` | int |
| `idEmp` | int |
| `idHie` | int |
| `Area` | int |
| `idImp` | int |
| `idUrg` | int |
| `nImp` | tinyint |
| `nUrg` | tinyint |
| `flgReincidente` | bit |
| `flgRecorrente` | bit |
| `flgN1Reg` | bit |
| `flgN1Conc` | bit |
| `tpAgenteReg` | char |
| `idFluPai` | int |
| `idProcPai` | int |
| `idTpSla` | int |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
