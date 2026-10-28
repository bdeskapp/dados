---
gerado: sincronizacao
---

# dbo.SyncEmailAddress

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAddress` | INT | não | sim | não |
| `idConnect` | INT | não | não | não |
| `dsTo` | VARCHAR(100) | não | não | não |
| `flgKeepMessages` | BIT | não | não | não |
| `sTempDir` | VARCHAR(500) | sim | não | não |
| `nRetentionDays` | TINYINT | sim | não | não |
| `nLogDays` | TINYINT | sim | não | não |
| `sLogContact` | VARCHAR(500) | sim | não | não |
| `flgSendToScreening` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailAddress` (idConnect) → `dbo.SyncEmailConnect` (idConnect)
- `dbo.SyncEmailNewReq` (idAddress) → `dbo.SyncEmailAddress` (idAddress)
- `dbo.SyncEmailUpdateReq` (idAddress) → `dbo.SyncEmailAddress` (idAddress)
