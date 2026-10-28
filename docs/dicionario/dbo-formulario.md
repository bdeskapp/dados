---
gerado: sincronizacao
---

# dbo.Formulario

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `cdFrm` | INT | não | não | não |
| `vsFrm` | TINYINT | não | não | não |
| `dsFrm` | VARCHAR(50) | não | não | não |
| `obsFrm` | VARCHAR(500) | sim | não | não |
| `flgFrmAtivo` | BIT | não | não | não |
| `flgFrmDisponivel` | BIT | não | não | não |
| `idAre` | INT | sim | não | não |
| `tpControlaCusto` | CHAR(1) | não | não | não |
| `tpControlaHora` | CHAR(1) | não | não | não |
| `tpLocalizacao` | CHAR(1) | não | não | não |
| `flgOffline` | BIT | não | não | não |
| `flgAgenda` | BIT | não | não | não |
| `nPrazoMinimo` | INT | não | não | não |
| `flgRecorrente` | BIT | não | não | não |
| `tpReporteHora` | CHAR(1) | sim | não | não |
| `flgInterno` | BIT | não | não | não |
| `idGruAdm` | INT | não | não | não |
| `flgDirecionaArea` | BIT | não | não | não |
| `flgDirecionaAtividade` | BIT | não | não | não |
| `flgAbreArea` | BIT | não | não | não |
| `flgMultipla` | BIT | não | não | não |
| `flgKBKeyword` | BIT | não | não | não |
| `flgKBInd` | BIT | não | não | não |
| `flgVIP` | BIT | não | não | não |
| `flgKBContrib` | BIT | não | não | não |
| `email` | VARCHAR(100) | sim | não | não |
| `tpPrazo` | CHAR(1) | não | não | não |
| `idUsuAutor` | INT | sim | não | não |
| `dtInclusao` | DATETIME | sim | não | não |
| `idUsuRevisor` | INT | sim | não | não |
| `dtAlteracao` | DATETIME | sim | não | não |
| `dtValidacao` | DATETIME | sim | não | não |
| `qtdErros` | SMALLINT | sim | não | não |
| `qtdAlertas` | SMALLINT | sim | não | não |
| `qtdRecomenda` | SMALLINT | sim | não | não |
| `dsFrmComp` | VARCHAR(90) | sim | não | não |
| `idCatProc` | SMALLINT | sim | não | não |
| `tpPartProc` | CHAR(1) | não | não | não |
| `tpRotina` | CHAR(1) | sim | não | não |
| `idMascara` | INT | sim | não | não |
| `cdProcITIL` | CHAR(3) | sim | não | não |
| `flgContribDefault` | BIT | não | não | não |
| `dsAnexarDoc` | VARCHAR(500) | sim | não | não |
| `flgFiltrarTipoTarefa` | BIT | não | não | não |
| `flgRequerAprovacao` | BIT | não | não | não |
| `idFrmStatusAprovacao` | INT | sim | não | não |
| `idFrmPapelAprovador` | INT | sim | não | não |
| `flgAprovacaoAutomatica` | BIT | não | não | não |
| `flgApontamentoHoraAcao` | BIT | não | não | não |
| `idFrmStatusDefinirAprovador` | INT | sim | não | não |
| `flgVINCMes` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReq` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Condicao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.DadContextoCampo` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Favoritos` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormAcao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormAcesso` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormCategoria` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormDespesa` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormLocaliza` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormOrigem` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormPapel` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormPriMatriz` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormPri` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormRelac` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormRelac` (idFrmRelac) → `dbo.Formulario` (idFrm)
- `dbo.FormSLA` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormStatus` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormTipoDoc` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormTipoTarefa` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormValida` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Formulario` (idAre) → `dbo.Area` (idAre)
- `dbo.Formulario` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.Formulario` (idFrmStatusDefinirAprovador) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Formulario` (idFrmPapelAprovador) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Formulario` (idFrmStatusAprovacao) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Formulario` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.Formulario` (idMascara) → `dbo.Mascara` (idMascara)
- `dbo.Formulario` (cdProcITIL) → `dbo.ProcessoITIL` (cdITIL)
- `dbo.Formulario` (idUsuAutor) → `dbo.Usuario` (idUsu)
- `dbo.Formulario` (idUsuRevisor) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.ItemCardapio` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.KBRotina` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.LicConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Gru` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Hie` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_KBUtil` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MetricaCalc_Pat` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Minuta` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.MuralFormulario` (idFormulario) → `dbo.Formulario` (idFrm)
- `dbo.PatOperacao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Processo` (idFrmAut) → `dbo.Formulario` (idFrm)
- `dbo.Relacao` (idFrmCausa) → `dbo.Formulario` (idFrm)
- `dbo.Relacao` (idFrmEfeito) → `dbo.Formulario` (idFrm)
- `dbo.Req` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.RotinaFavorita` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Rotina` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.ServicoAtend` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailNewReq` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailUpdateReq` (idFrm) → `dbo.Formulario` (idFrm)
