---
gerado: sincronizacao
---
# Fora de escopo: workflow (processo e fluxo)


**O que é.** O motor que define um processo em etapas (rotinas) e acompanha cada execução desse processo como um fluxo de requisições. Esta documentação do banco não detalha o motor.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `Processo` | a definição do processo (`cdProc`, `dsProc`, `vsProc`, `idAre`, `idGruAdm`) |
| `Rotina` | as etapas do processo (`idProc`, `idFrm`, `idTar`, `nSeq`, `dsRotina`) |
| `RotinaTransicao` | liga uma rotina a uma transição de formulário (`idRotina`, `idFrmTrans`) |
| `Workflow` | a execução de um processo: `idFlu`, `idProc`, `idRotinaAtual`, `dtInicio`, `dtFim` |
| `WorkflowPlan` | o planejado e o realizado por rotina de uma execução (`idFlu`, `idRotina`, `idReq`, `dtIniPrev`, `dtFimPrev`, `dtIniReal`, `dtFimReal`) |
| `Fluxo`, `FluxoTarefa` | catálogo de fluxos de atividades; `FluxoTarefa` liga `Fluxo` a `Tarefa`. O banco não traz FK entre `Fluxo` e `Workflow`; as duas tabelas têm uma coluna `idFlu` cada |


## Onde toca a requisição

- `Req.idFlu` e `ReqConcluida.idFlu` têm FK para `Workflow.idFlu`; `idFluPai` aponta para o fluxo pai. Ver [requisição, seção Fluxo](../fatos/requisicao.md).
- `Req.idRotina` e `Req.idRotinaProcPai` (e as mesmas colunas em `ReqConcluida`) têm FK para `Rotina`.
- `WorkflowPlan.idReq` é a requisição da rotina planejada (coluna sem FK).
- Para identificar requisição de fluxo, use `Req.idFlu` preenchido. O canal `P` de `Req.tpAgenteReg` marca a abertura de requisição de fluxo pela rotina automática e pela tela de abertura de fluxo, e requisições de fluxo também têm outros códigos de canal; ver [canal de origem](../dimensoes/canal-origem.md).

## Veja também

[Requisição](../fatos/requisicao.md) · [Status e fase](../dimensoes/status-fase.md) · [Índice](../busca.md)
