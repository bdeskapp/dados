---
gerado: sincronizacao
---

# dbo.ReqPartConcluida

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqPart` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idFrmPapel` | INT | não | não | não |
| `dsPapel` | VARCHAR(50) | não | não | não |
| `nmPart` | VARCHAR(100) | sim | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `tpReporteDespesa` | CHAR(1) | não | não | não |
| `dtUltimoAcesso` | DATETIME | sim | não | não |
| `flgFinanceiro` | BIT | não | não | não |
| `flgReportaHora` | BIT | não | não | não |
| `idPart` | INT | não | não | não |
| `idTpPapel` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqDespConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqDocAcessoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqDocConcluida` (idReqPartOwner) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqHistAcessoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqHistConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqMsgAcessoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqMsgConcluida` (idRemetente) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqPartConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqPartConcluida` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.ReqPendConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqTimeAdoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
