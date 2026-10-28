---
gerado: sincronizacao
---

# dbo.RequestHistory

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idReqHist` | int |
| `idReq` | int |
| `idReqPart` | int |
| `nmPart` | varchar |
| `idGru` | int |
| `dsGru` | varchar |
| `idUsu` | int |
| `nmUsu` | varchar |
| `idFrmAcao` | int |
| `dsAcao` | varchar |
| `idMotivo` | int |
| `dsMotivo` | varchar |
| `dsReqHist` | text |
| `idFrmStatus` | int |
| `dsSta` | varchar |
| `dtIniReqHist` | datetime |
| `dtFimReqHist` | datetime |
| `tpRegistro` | char |
| `flgPublico` | bit |
| `idPersona` | int |
| `nmPersona` | varchar |
| `dtRegistro` | datetime |
| `flgSYS` | bit |
| `idFlu` | int |
| `dsTitulo` | varchar |
| `flgNotBloq` | bit |
| `idReqPartADO` | int |
| `flgContaSLA` | bit |
| `flgCalc` | bit |
| `idJus` | int |
| `dsNotLog` | varchar |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
