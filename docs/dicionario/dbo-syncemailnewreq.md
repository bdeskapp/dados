---
gerado: sincronizacao
---

# dbo.SyncEmailNewReq

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNewReqByEmail` | INT | não | sim | não |
| `idAddress` | INT | não | não | não |
| `idFrm` | INT | não | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `idFrmTpDoc` | INT | sim | não | não |
| `flgExtern` | BIT | não | não | não |
| `flgAnexos` | BIT | não | não | não |
| `nMinDuplicate` | TINYINT | não | não | não |
| `idTpPapelAdo` | SMALLINT | sim | não | não |
| `idPartAdo` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `flgEnabled` | BIT | não | não | não |
| `flgInserirPapelCOP` | BIT | não | não | não |
| `tpDuplicate` | CHAR(1) | sim | não | não |
| `flgAnteFixo` | BIT | não | não | não |
| `idUsuAnteFixo` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailNewReqCat` (idNewReqByEmail) → `dbo.SyncEmailNewReq` (idNewReqByEmail)
- `dbo.SyncEmailNewReq` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.SyncEmailNewReq` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailNewReq` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailNewReq` (idTpPapelAdo, idPartAdo) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.SyncEmailNewReq` (idAddress) → `dbo.SyncEmailAddress` (idAddress)
- `dbo.SyncEmailNewReq` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.SyncEmailNewReq` (idUsuAnteFixo) → `dbo.Usuario` (idUsu)
