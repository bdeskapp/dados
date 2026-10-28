---
gerado: sincronizacao
---

# dbo.FormPapel

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `idPapel` | INT | não | não | não |
| `dsPapel` | VARCHAR(50) | não | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `idPapelDefault` | INT | sim | não | não |
| `flgMultiplo` | BIT | não | não | não |
| `flgCombinado` | BIT | não | não | não |
| `tpReporteDespesa` | CHAR(1) | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `flgDefFinanceiro` | BIT | não | não | não |
| `flgReportaHora` | BIT | não | não | não |
| `idTpPapelDefault` | SMALLINT | sim | não | não |
| `idPartDefault` | INT | sim | não | não |
| `flgDefaultOpcional` | BIT | sim | não | não |
| `flgLinha` | BIT | não | não | não |
| `tpApresentacao` | VARCHAR(1) | não | não | não |
| `dsToolTip` | VARCHAR(100) | sim | não | não |
| `tpPart` | TINYINT | não | não | não |
| `flgAcesso` | BIT | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReqPart` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.CondPapelAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.CondPapelPartAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.CondPapel` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormLocaliza` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormNotificacaoAlerta` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormNotificacao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelCombinado` (idFrmPapelCombinado) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelCombinado` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelObrigatorioDadoAdicional` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelObrigatorioTarefa` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelPatDom` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelPat` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelRelacionado` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelRelacionado` (idFrmPapelRelacionado) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelStatus` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelTipo` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapel` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormPapel` (idPapel) → `dbo.Papel` (idPapel)
- `dbo.FormPapel` (idTpPapelDefault) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormRequerAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Formulario` (idFrmPapelAprovador) → `dbo.FormPapel` (idFrmPapel)
- `dbo.ProcHistAcesso` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.QPOQQ` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAcao` (idFrmPapelOrigem) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAcao` (idFrmPapelDestino) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAlertaDest` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.ReqParticipante` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RotinaMapaPapel` (idFrmPapelOrigem) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RotinaMapaPapel` (idFrmPapelDestino) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Rotina` (idAcessoIni) → `dbo.FormPapel` (idFrmPapel)
- `dbo.Rotina` (idAcessoFim) → `dbo.FormPapel` (idFrmPapel)
