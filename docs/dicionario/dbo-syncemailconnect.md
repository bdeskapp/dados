---
gerado: sincronizacao
---

# dbo.SyncEmailConnect

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idConnect` | INT | não | sim | não |
| `sProtocol` | CHAR(10) | não | não | não |
| `nmServer` | VARCHAR(100) | não | não | não |
| `nPort` | SMALLINT | não | não | não |
| `nmUser` | VARCHAR(100) | não | não | não |
| `flgSSL` | BIT | não | não | não |
| `sTempDir` | VARCHAR(500) | não | não | não |
| `nRetentionDays` | TINYINT | não | não | não |
| `nLogDays` | TINYINT | não | não | não |
| `sLogContact` | VARCHAR(500) | sim | não | não |
| `clientId` | VARCHAR(100) | sim | não | não |
| `tenant` | VARCHAR(100) | sim | não | não |
| `tpAutenticacao` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailAddress` (idConnect) → `dbo.SyncEmailConnect` (idConnect)
