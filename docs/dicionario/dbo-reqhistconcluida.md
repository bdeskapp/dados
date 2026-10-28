---
gerado: sincronizacao
---

# dbo.ReqHistConcluida

**Selo:** Explicada

Explicada em:

- [ação](../dimensoes/acao.md)
- [eventos do histórico](../fatos/eventos-historico.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqHist` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | sim | não | não |
| `nmPart` | VARCHAR(100) | sim | não | não |
| `idGru` | INT | sim | não | não |
| `dsGru` | VARCHAR(50) | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `nmUsu` | VARCHAR(100) | sim | não | não |
| `idFrmAcao` | INT | sim | não | não |
| `dsAcao` | VARCHAR(30) | sim | não | não |
| `idMotivo` | INT | sim | não | não |
| `dsMotivo` | VARCHAR(100) | sim | não | não |
| `dsReqHist` | TEXT | sim | não | não |
| `idFrmStatus` | INT | sim | não | não |
| `dsSta` | VARCHAR(30) | sim | não | não |
| `dtIniReqHist` | DATETIME | não | não | não |
| `dtFimReqHist` | DATETIME | sim | não | não |
| `tpRegistro` | CHAR(1) | não | não | não |
| `flgPublico` | BIT | não | não | não |
| `idPersona` | INT | sim | não | não |
| `nmPersona` | VARCHAR(100) | sim | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `flgSYS` | BIT | não | não | não |
| `idFlu` | INT | sim | não | não |
| `dsTitulo` | VARCHAR(100) | sim | não | não |
| `flgNotBloq` | BIT | não | não | não |
| `idReqPartADO` | INT | sim | não | não |
| `flgContaSLA` | BIT | não | não | não |
| `idJus` | INT | sim | não | não |
| `dsNotLog` | VARCHAR(MAX) | sim | não | não |
| `dtTimeOutManual` | DATETIME | sim | não | não |
| `flgOcultarHistorico` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqHistAcessoConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqHistConcluida` (idJus) → `dbo.Justificativa` (idJus)
- `dbo.ReqHistConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqHistConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqMinutaConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqMinutaHistConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqMsgConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqMsgConcluida` (idReqHistRelac) → `dbo.ReqHistConcluida` (idReqHist)
- `dbo.ReqUltHistConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
