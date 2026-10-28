---
gerado: sincronizacao
---

# dbo.ReqHistorico

**Selo:** Explicada

Explicada em:

- [ação](../dimensoes/acao.md)
- [eventos do histórico](../fatos/eventos-historico.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqHist` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `idFrmAcao` | INT | sim | não | não |
| `idMotivo` | INT | sim | não | não |
| `dsReqHist` | TEXT | sim | não | não |
| `idFrmStatus` | INT | sim | não | não |
| `dtIniReqHist` | DATETIME | não | não | não |
| `dtFimReqHist` | DATETIME | sim | não | não |
| `tpRegistro` | CHAR(1) | não | não | não |
| `flgPublico` | BIT | não | não | não |
| `idPersona` | INT | sim | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `flgSYS` | BIT | não | não | não |
| `idFlu` | INT | sim | não | não |
| `flgNotBloq` | BIT | não | não | não |
| `idReqPartADO` | INT | sim | não | não |
| `flgContaSLA` | BIT | não | não | não |
| `flgCalc` | BIT | não | não | não |
| `idJus` | INT | sim | não | não |
| `dsNotLog` | VARCHAR(MAX) | sim | não | não |
| `dtTimeOutManual` | DATETIME | sim | não | não |
| `flgOcultarHistorico` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqHistAcesso` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqHistorico` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.ReqHistorico` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.ReqHistorico` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.ReqHistorico` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ReqHistorico` (idJus) → `dbo.Justificativa` (idJus)
- `dbo.ReqHistorico` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqHistorico` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqHistorico` (idPersona) → `dbo.Usuario` (idUsu)
- `dbo.ReqHistorico` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ReqMensagem` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMensagem` (idReqHistRelac) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMinutaHistorico` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMinuta` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqProblema` (idReqHistCAU) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqProblema` (idReqHistWKA) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqProblema` (idReqHistSOL) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqUltHist` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
