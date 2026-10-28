---
gerado: sincronizacao
---

# dbo.FormStatus

**Selo:** Explicada

Explicada em:

- [status](../dimensoes/status-fase.md)
- [tempo por status](../fatos/tempo-por-status.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmStatus` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `idSta` | INT | não | não | não |
| `dsSta` | VARCHAR(30) | não | não | não |
| `flgContaSLA` | BIT | não | não | não |
| `valTimeout` | SMALLINT | sim | não | não |
| `idFrmAcaoTimeout` | INT | sim | não | não |
| `idMotivoTimeout` | INT | sim | não | não |
| `flgFluxo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `tpCongelamento` | CHAR(1) | sim | não | não |

## Chaves estrangeiras

- `dbo.Causa` (idFrmStatusTO) → `dbo.FormStatus` (idFrmStatus)
- `dbo.ColunaMuralStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.CondStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormNotListaStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormNotificacaoAlerta` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormPapelStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormRelacStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormStatus` (idFrmAcaoTimeout) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormStatus` (idMotivoTimeout) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.FormStatus` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormStatus` (idSta) → `dbo.Status` (idSta)
- `dbo.FormTransicao` (idFrmStatusAtual) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormTransicao` (idFrmStatusProx) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Formulario` (idFrmStatusDefinirAprovador) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Formulario` (idFrmStatusAprovacao) → `dbo.FormStatus` (idFrmStatus)
- `dbo.QPOQQ` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoEfeito` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoTimeout` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.ReqHistorico` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Req` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
