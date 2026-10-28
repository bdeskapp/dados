---
gerado: sincronizacao
---

# dbo.vwReqDocTotal

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idDoc` | int |
| `idDocOriginal` | int |
| `nVersao` | tinyint |
| `idReq` | int |
| `nmDocFisico` | varchar |
| `dsTitulo` | varchar |
| `idReqPartOwner` | int |
| `dtInclusao` | smalldatetime |
| `dtInvalidacao` | smalldatetime |
| `flgInvalido` | bit |
| `flgPublico` | bit |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
