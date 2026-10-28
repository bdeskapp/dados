---
gerado: sincronizacao
---

# dbo.ReqParticipante

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqPart` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idFrmPapel` | INT | não | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `tpReporteDespesa` | CHAR(1) | não | não | não |
| `dtUltimoAcesso` | DATETIME | sim | não | não |
| `flgFinanceiro` | BIT | não | não | não |
| `flgReportaHora` | BIT | não | não | não |
| `idPart` | INT | não | não | não |
| `idTpPapel` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqDespesa` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqDocAcesso` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqDocumento` (idReqPartOwner) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqHistAcesso` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqHistorico` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqKB` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqMensagem` (idRemetente) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqMsgAcesso` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqParticipante` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.ReqParticipante` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqParticipante` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.ReqPendencia` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqTimeAdo` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
