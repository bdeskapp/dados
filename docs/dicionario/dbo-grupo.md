---
gerado: sincronizacao
---

# dbo.Grupo

**Selo:** Explicada

Explicada em:

- [grupo e área](../dimensoes/grupo-area.md)
- [calendário de atendimento](../dimensoes/tempo-calendario.md)
- [tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `dsGru` | VARCHAR(50) | não | não | não |
| `idCan` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `flgGruAtivo` | BIT | não | não | não |
| `idOpe` | INT | sim | não | não |
| `celular` | VARCHAR(15) | sim | não | não |
| `idOpePager` | INT | sim | não | não |
| `pager` | VARCHAR(15) | sim | não | não |
| `tpAlerta` | TINYINT | sim | não | não |
| `nivelAlerta` | TINYINT | sim | não | não |
| `flgMailAbertura` | BIT | sim | não | não |
| `flgMsgLiberacaoWF` | BIT | sim | não | não |
| `idAre` | INT | não | não | não |
| `flgEnviaDsOsAbertura` | BIT | não | não | não |
| `flgPermiteDirecionamentoAnexo` | BIT | não | não | não |
| `flgConfirmacaoDirecionamentoAnexo` | BIT | não | não | não |
| `flgAtendeReq` | BIT | não | não | não |
| `nNivel` | TINYINT | sim | não | não |
| `tpAssume` | TINYINT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaOS` (IdGru) → `dbo.Grupo` (idGru)
- `dbo.AgendaReq` (idGruResponsavel) → `dbo.Grupo` (idGru)
- `dbo.Area` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.Area` (idGruKB) → `dbo.Grupo` (idGru)
- `dbo.Aviso` (idGru) → `dbo.Grupo` (idGru)
- `dbo.CompMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ComponenteMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.FluxoOsAnexoGrupo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.FormTransGrupoSolucionador` (idGru) → `dbo.Grupo` (idGru)
- `dbo.Formulario` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.GerenciaGrupo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.GrupoParticipante` (idGru) → `dbo.Grupo` (idGru)
- `dbo.Grupo` (idAre) → `dbo.Area` (idAre)
- `dbo.Grupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Grupo` (idCan) → `dbo.CalendarioNome` (idCan)
- `dbo.Justificativa` (idGru) → `dbo.Grupo` (idGru)
- `dbo.KBAcesso` (idGru) → `dbo.Grupo` (idGru)
- `dbo.KBClasse` (idGruAprov) → `dbo.Grupo` (idGru)
- `dbo.KBClasse` (idGruAvalia) → `dbo.Grupo` (idGru)
- `dbo.KBase` (idGruResp) → `dbo.Grupo` (idGru)
- `dbo.LicConfig` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.LicencaMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ListaDistribMembros` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ListaDistrib` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.Mascara` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.MetricaCalc_Gru` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MetricaCalc_KBUtil` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MetricaCalc_KB` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MonitorConfigAlerta` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OS` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OS` (idGruAbertura) → `dbo.Grupo` (idGru)
- `dbo.ObjectSummary` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OsFluxo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.PatrimonioAtributoSolicitacao` (idGru) → `dbo.Grupo` (idGru)
- `dbo.Processo` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.ReqHistorico` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ReqKB` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ReqRecatConcluida` (idGruAnt) → `dbo.Grupo` (idGru)
- `dbo.ReqRecatConcluida` (idGruAtual) → `dbo.Grupo` (idGru)
- `dbo.ReqRecat` (idGruAnt) → `dbo.Grupo` (idGru)
- `dbo.ReqRecat` (idGruAtual) → `dbo.Grupo` (idGru)
- `dbo.Req` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ServicoAtend` (idGruAtend) → `dbo.Grupo` (idGru)
- `dbo.SyncEmailNewReqCat` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupoAprovador` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupoHistorico` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TipoPatrimonio` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.UsuarioGrupoPrcEscalonamento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.UsuarioGrupo` (idGru) → `dbo.Grupo` (idGru)
