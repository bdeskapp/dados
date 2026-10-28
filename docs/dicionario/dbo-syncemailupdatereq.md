---
gerado: sincronizacao
---

# dbo.SyncEmailUpdateReq

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUpdateReqByEmail` | INT | não | sim | não |
| `idAddress` | INT | não | não | não |
| `idFrm` | INT | não | não | não |
| `idFrmTpDoc` | INT | sim | não | não |
| `flgNoKeyword` | BIT | não | não | não |
| `flgNoAccess` | BIT | não | não | não |
| `flgNoParticipant` | BIT | não | não | não |
| `dsNotificationText` | VARCHAR(150) | sim | não | não |
| `flgEnabled` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailActionUpdate` (idUpdateReqByEmail) → `dbo.SyncEmailUpdateReq` (idUpdateReqByEmail)
- `dbo.SyncEmailUpdateReq` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailUpdateReq` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailUpdateReq` (idAddress) → `dbo.SyncEmailAddress` (idAddress)
