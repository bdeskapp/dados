---
gerado: sincronizacao
---

# dbo.FormAcao

**Selo:** Explicada

Explicada em:

- [ação](../dimensoes/acao.md)
- [eventos do histórico](../fatos/eventos-historico.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmAcao` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `idAcao` | INT | não | não | não |
| `dsAcao` | VARCHAR(30) | não | não | não |
| `flgMotivo` | BIT | não | não | não |
| `flgHistorico` | BIT | não | não | não |
| `flgFluxo` | BIT | não | não | não |
| `flgInterna` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgDireta` | BIT | não | não | não |
| `flgResp` | BIT | não | não | não |
| `flgTimeOutManual` | BIT | não | não | não |
| `flgConclusao` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Causa` (idFrmAcaoDireta) → `dbo.FormAcao` (idFrmAcao)
- `dbo.CondicaoAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.DadFormAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormAcaoMotivo` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.FormAcao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormNotLista` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormNotificacao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRelacAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRequerAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRequerAcao` (idFrmAcaoRequerida) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormStatus` (idFrmAcaoTimeout) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormTransicao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.Notificacao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.QPOQQ` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.RelacaoAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.Relacao` (idFrmAcaoOrigem) → `dbo.FormAcao` (idFrmAcao)
- `dbo.ReqHistorico` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.SyncEmailActionUpdate` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
