---
gerado: sincronizacao
---

# dbo.ReqDocConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDoc` | INT | não | sim | não |
| `idDocOriginal` | INT | não | não | não |
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

- `dbo.ReqDocAcessoConcluida` (idDoc) → `dbo.ReqDocConcluida` (idDoc)
- `dbo.ReqDocConcluida` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.ReqDocConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqDocConcluida` (idReqPartOwner) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqDocConcluida` (idFlu) → `dbo.Workflow` (idFlu)
