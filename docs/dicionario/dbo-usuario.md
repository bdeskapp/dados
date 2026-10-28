---
gerado: sincronizacao
---

# dbo.Usuario

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)
- [eventos do histórico](../fatos/eventos-historico.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `login` | VARCHAR(81) | não | não | não |
| `nmUsu` | VARCHAR(100) | sim | não | não |
| `email` | VARCHAR(1000) | sim | não | não |
| `idPer` | INT | sim | não | não |
| `estacao` | VARCHAR(20) | sim | não | não |
| `matricula` | VARCHAR(50) | sim | não | não |
| `fone` | VARCHAR(17) | sim | não | não |
| `ramal` | VARCHAR(8) | sim | não | não |
| `celular` | VARCHAR(18) | sim | não | não |
| `idOpe` | INT | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `idDom` | INT | sim | não | não |
| `valorHora` | MONEY | sim | não | não |
| `dtIniUsu` | DATETIME | não | não | não |
| `dtFimUsu` | DATETIME | sim | não | não |
| `flgUsuAtivo` | BIT | não | não | não |
| `idUsuSuperiorHierarquico` | INT | sim | não | não |
| `flgAtendeReq` | BIT | não | não | não |
| `flgPartGrupo` | BIT | não | não | não |
| `idObjDefault` | INT | sim | não | não |
| `cdIdioma` | CHAR(5) | sim | não | não |
| `dtBloqueio` | DATETIME | sim | não | não |
| `dtAcesso` | DATETIME | sim | não | não |
| `idUsuSuperiorAlternativo` | INT | sim | não | não |
| `flgAprovaReq` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |
| `flgPermiteLoginBDesk` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ASKCodeLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ASKCode` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.AgendaReq` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.AplicacaoExterna` (idUsuAtualizacao) → `dbo.Usuario` (idUsu)
- `dbo.AutoAtendimento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Contato` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.CRM_ContratoDoc` (idOwner) → `dbo.Usuario` (idUsu)
- `dbo.CRM_FatAcesso` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Faturamento` (idUsuPreparo) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Faturamento` (idUsuConfirm) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Gestor` (idGestor) → `dbo.Usuario` (idUsu)
- `dbo.CalendarioNome` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Calendario` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.CompAlertaNotifica` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.CompMovimento` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.CompMovimento` (idUsuMov) → `dbo.Usuario` (idUsu)
- `dbo.ComponenteAlerta` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.DadLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.DadValorPatSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
- `dbo.DadoAdicionalUsuarioLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.DadoAdicionalUsuarioLog` (idUsuInclusao) → `dbo.Usuario` (idUsu)
- `dbo.DadoAdicionalUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.DocusignReq` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Efeito` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Favoritos` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Feriado` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.FiltroListaAcompanhamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Formulario` (idUsuAutor) → `dbo.Usuario` (idUsu)
- `dbo.Formulario` (idUsuRevisor) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcessoTipoPapel` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcessoUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcessoUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.GrupoAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.GrupoParticipante` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Grupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idUsu1) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idUsu2) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idUsu3) → `dbo.Usuario` (idUsu)
- `dbo.Justificativa` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.KBase` (idAutor) → `dbo.Usuario` (idUsu)
- `dbo.KBase` (idRevisor) → `dbo.Usuario` (idUsu)
- `dbo.LicAlerta` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.LicConfig` (idUsuSolicitante) → `dbo.Usuario` (idUsu)
- `dbo.LicReserva` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.LicencaAlerta` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.LicencaMovimento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.LicencaMovimento` (idUsuSolic) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistribMembros` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistribMembros` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistrib` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistrib` (idUsuAlter) → `dbo.Usuario` (idUsu)
- `dbo.ListaICClasseTipo` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICClasseTipo` (idUsuFim) → `dbo.Usuario` (idUsu)
- `dbo.ListaICListaAdminitrador` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICListaAdminitrador` (idUsuFim) → `dbo.Usuario` (idUsu)
- `dbo.ListaICUsuario` (idUsuAss) → `dbo.Usuario` (idUsu)
- `dbo.ListaICUsuario` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICUsuario` (idUsuFim) → `dbo.Usuario` (idUsu)
- `dbo.ListaIC` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ListaIC` (idUsuChange) → `dbo.Usuario` (idUsu)
- `dbo.LogKB` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.MetricaCalc_KBUtil` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Minuta` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.MonitorConfigAlerta` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.MonitorConfig` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.NotificacaoDocUsu` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Notificacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.OSFluxoProjeto` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.OS` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.OS` (idUsuAbertura) → `dbo.Usuario` (idUsu)
- `dbo.OS` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.OrgHierarquia` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.OsAnexoConcluida` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.OsAnexo` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.ParametroAvancado` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.PatAlertaResumo` (idUsuDest) → `dbo.Usuario` (idUsu)
- `dbo.PatAlerta` (idUsuOp) → `dbo.Usuario` (idUsu)
- `dbo.PatDocumento` (idOwner) → `dbo.Usuario` (idUsu)
- `dbo.PatLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.PatMovimento` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAssociadoSolicitacao` (idUsuAss) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAssociadoSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAtributoSolicitacao` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAtributoSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
- `dbo.Patrimonio` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.PercentualEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.PesqRespUsuario` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Processo` (idUsuAutor) → `dbo.Usuario` (idUsu)
- `dbo.Processo` (idUsuRevisor) → `dbo.Usuario` (idUsu)
- `dbo.RegistroLigacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RegistroLigacao` (idAtendente) → `dbo.Usuario` (idUsu)
- `dbo.RepAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.RepPesquisaAgendadaUsu` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RepSave` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RepWork` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqApontAprov` (idUsuAprov) → `dbo.Usuario` (idUsu)
- `dbo.ReqAvaliacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqDespesa` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqHistorico` (idPersona) → `dbo.Usuario` (idUsu)
- `dbo.ReqHistorico` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqKB` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqMinutaHistConcluida` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqMinutaHistorico` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqPendConcluida` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqPendencia` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqRecatConcluida` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqRecat` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RequisicaoLog` (usuarioLog) → `dbo.Usuario` (idUsu)
- `dbo.Req` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.RotinaFavorita` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.SMSNotificacaoUsu` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ScheduledReportSubscriber` (SubscriberID) → `dbo.Usuario` (idUsu)
- `dbo.Sessao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Sistema_Log` (usuarioLog) → `dbo.Usuario` (idUsu)
- `dbo.SyncEmailConfig` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.SyncEmailNewReq` (idUsuAnteFixo) → `dbo.Usuario` (idUsu)
- `dbo.TabelaAdmin` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TabelaCompartilhada` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TabelaLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TarefaAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.TarefaGrupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.TarefaParticipanteAprovador` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Tarefa` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.TipoEscalonamentoPercentual` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TipoEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioCampoLayout` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioCategoria_ItemCardapio` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioGrupoPrcEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioGrupo` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioGrupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioHierarquia` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioHierarquia` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioLog` (idUsuResponsavelLog) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioPatrimonioSolicitacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioPatrimonioSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioPatrimonio` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.Usuario` (idDom) → `dbo.Dominio` (idDom)
- `dbo.Usuario` (cdIdioma) → `dbo.Idioma` (cdIdioma)
- `dbo.Usuario` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Usuario` (idObjDefault) → `dbo.Objeto` (idObj)
- `dbo.Usuario` (idPer) → `dbo.Perfil` (idPer)
- `dbo.Usuario` (idUsuSuperiorHierarquico) → `dbo.Usuario` (idUsu)
- `dbo.Usuario` (idUsuSuperiorAlternativo) → `dbo.Usuario` (idUsu)
- `dbo.Usuario` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.VIP` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.WorkflowPlan` (idUsu) → `dbo.Usuario` (idUsu)
