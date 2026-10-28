---
gerado: sincronizacao
---

# dbo.Tarefa

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | sim | não |
| `dsTar` | VARCHAR(100) | sim | não | não |
| `idSca` | INT | não | não | não |
| `idTpta` | INT | não | não | não |
| `idTpSla` | INT | não | não | não |
| `flgTarAtivo` | BIT | não | não | não |
| `slaTarPadrao` | INT | sim | não | não |
| `flgElegivel` | BIT | não | não | não |
| `dsTarComp` | VARCHAR(350) | sim | não | não |
| `idCat` | INT | sim | não | não |
| `flgSomenteFluxo` | BIT | não | não | não |
| `obsTar` | VARCHAR(1000) | sim | não | não |
| `dsCond` | VARCHAR(200) | sim | não | não |
| `tpCriticidade` | TINYINT | não | não | não |
| `flgSomenteAgenda` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgRecorrente` | BIT | não | não | não |
| `flgRecat` | BIT | não | não | não |
| `idMascara` | INT | sim | não | não |
| `flgDoc` | BIT | não | não | não |
| `dsAlertaDoc` | VARCHAR(300) | sim | não | não |
| `idLstSMS` | INT | sim | não | não |
| `txtSMS` | VARCHAR(MAX) | sim | não | não |
| `flgSMSAltera` | BIT | sim | não | não |
| `flgRecatExcetoSD` | BIT | não | não | não |
| `nTempoLembrete` | INT | sim | não | não |
| `tpAprovadores` | VARCHAR(2) | sim | não | não |
| `labelAprovadores` | VARCHAR(50) | sim | não | não |
| `flgVinculoObrigatorio` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaOS` (IdTar) → `dbo.Tarefa` (idTar)
- `dbo.AgendaReq` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.CondTarefaAcao` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.DadContextoCampo` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.FluxoTarefa` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.FormPapelObrigatorioTarefa` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.KBTarefa` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.LicConfig` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.MetricaCalc_Gru` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.MetricaCalc_Hie` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.MetricaCalc_Pat` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.Minuta` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.OSHistorico` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.OS` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.OS` (idTarAbertura) → `dbo.Tarefa` (idTar)
- `dbo.OsFluxo` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.PatOperacao` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecatConcluida` (idTarAnt) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecatConcluida` (idTarAtual) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecat` (idTarAnt) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecat` (idTarAtual) → `dbo.Tarefa` (idTar)
- `dbo.Req` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.Rotina` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.SyncEmailNewReqCat` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.SyncEmailNewReq` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaAcessoHistorico` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaAcesso` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaGrupoAprovador` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaGrupoHistorico` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaGrupo` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaParticipanteAprovador` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.Tarefa` (idCat) → `dbo.Categoria` (idCat)
- `dbo.Tarefa` (idLstSMS) → `dbo.ListaDistrib` (idLst)
- `dbo.Tarefa` (idMascara) → `dbo.Mascara` (idMascara)
- `dbo.Tarefa` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Tarefa` (idSca) → `dbo.SubCategoria` (idSca)
