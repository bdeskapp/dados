---
gerado: sincronizacao
---

# dbo.ReqDocumento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDoc` | INT | não | sim | não |
| `idDocOriginal` | INT | sim | não | não |
| `nVersao` | TINYINT | não | não | não |
| `idReq` | INT | não | não | não |
| `nmDocFisico` | VARCHAR(300) | não | não | não |
| `dsTitulo` | VARCHAR(255) | não | não | não |
| `idReqPartOwner` | INT | não | não | não |
| `dtInclusao` | SMALLDATETIME | não | não | não |
| `dtInvalidacao` | SMALLDATETIME | sim | não | não |
| `flgInvalido` | BIT | não | não | não |
| `flgPublico` | BIT | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idFrmTpDoc` | INT | sim | não | não |
| `idFlu` | INT | sim | não | não |
| `flgExcluido` | BIT | não | não | não |
| `dtExpiracao` | SMALLDATETIME | sim | não | não |
| `flgInline` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqDocAcesso` (idDoc) → `dbo.ReqDocumento` (idDoc)
- `dbo.ReqDocumento` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.ReqDocumento` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqDocumento` (idDocOriginal) → `dbo.ReqDocumento` (idDoc)
- `dbo.ReqDocumento` (idReqPartOwner) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqDocumento` (idFlu) → `dbo.Workflow` (idFlu)
