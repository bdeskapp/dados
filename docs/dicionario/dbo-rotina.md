---
gerado: sincronizacao
---

# dbo.Rotina

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotina` | INT | não | sim | não |
| `idProc` | INT | não | não | não |
| `idFrm` | INT | não | não | não |
| `idTar` | INT | sim | não | não |
| `idProcSub` | INT | sim | não | não |
| `nSeq` | TINYINT | não | não | não |
| `dsRotina` | VARCHAR(60) | sim | não | não |
| `flgAuto` | BIT | não | não | não |
| `flgVerbaObrigatoria` | BIT | não | não | não |
| `flgLocObrigatoria` | BIT | não | não | não |
| `flgLocEditavel` | BIT | não | não | não |
| `flgDescObrigatoria` | BIT | não | não | não |
| `flgAssuntoTarefa` | BIT | não | não | não |
| `flgPermiteMultPapeis` | BIT | não | não | não |
| `flgCombinaReg` | BIT | não | não | não |
| `tpRotina` | CHAR(1) | não | não | não |
| `idAcessoIni` | INT | sim | não | não |
| `idAcessoFim` | INT | sim | não | não |
| `flgRepeat` | BIT | não | não | não |
| `flgAprovAutomatica` | BIT | não | não | não |
| `flgHighlander` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReq` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Condicao` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.DadProcessoTarefa` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.DadProcesso` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Efeito` (idRotinaEfeito) → `dbo.Rotina` (idRotina)
- `dbo.ProcHistAcesso` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ProcHistAcesso` (idRotinaAcesso) → `dbo.Rotina` (idRotina)
- `dbo.ProcTipoDoc` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ProcessoRegraPlan` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ProcessoRegraPlan` (idRotinaPlan) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoAcao` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoAlertaDest` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoAtribuicao` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoAtribuicao` (idRotinaDestino) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoStatus` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Relacao` (idRotinaCausa) → `dbo.Rotina` (idRotina)
- `dbo.Relacao` (idRotinaEfeito) → `dbo.Rotina` (idRotina)
- `dbo.ReqConcluida` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ReqConcluida` (idRotinaProcPai) → `dbo.Rotina` (idRotina)
- `dbo.Req` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Req` (idRotinaProcPai) → `dbo.Rotina` (idRotina)
- `dbo.RotinaDepend` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.RotinaDepend` (idPredecessora) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaPapel` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaPapel` (idRotinaDestino) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaVar` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaVar` (idRotinaDestino) → `dbo.Rotina` (idRotina)
- `dbo.RotinaTransicao` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Rotina` (idAcessoIni) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Rotina` (idAcessoFim) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Rotina` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Rotina` (idProc) → `dbo.Processo` (idProc)
- `dbo.Rotina` (idProcSub) → `dbo.Processo` (idProc)
- `dbo.Rotina` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TransicaoCondicional` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.WorkflowPlan` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.Workflow` (idRotinaAtual) → `dbo.Rotina` (idRotina)
