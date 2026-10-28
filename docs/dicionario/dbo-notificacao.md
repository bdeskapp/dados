---
gerado: sincronizacao
---

# dbo.Notificacao

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNot` | INT | não | sim | não |
| `idFrmNot` | INT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `idReq` | INT | sim | não | não |
| `dsTitulo` | VARCHAR(8000) | sim | não | não |
| `dsNot` | TEXT | não | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `flgLida` | BIT | não | não | não |
| `dsErro` | VARCHAR(500) | sim | não | não |
| `emailErro` | VARCHAR(100) | sim | não | não |
| `dtErro` | DATETIME | sim | não | não |
| `nTentativa` | INT | sim | não | não |
| `email` | VARCHAR(100) | sim | não | não |
| `flgEnviarEmail` | BIT | não | não | não |
| `idFrmNotAlerta` | INT | sim | não | não |
| `idFrmAcao` | INT | sim | não | não |
| `dsErroPush` | VARCHAR(500) | sim | não | não |
| `dtEnvioPush` | DATETIME | sim | não | não |
| `dtErroPush` | DATETIME | sim | não | não |
| `nTentativasPush` | INT | não | não | não |
| `dtResumoPush` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.Notificacao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.Notificacao` (idFrmNot) → `dbo.FormNotificacao` (idFrmNot)
- `dbo.Notificacao` (idFrmNotAlerta) → `dbo.FormNotificacaoAlerta` (idFrmNotAlerta)
- `dbo.Notificacao` (idUsu) → `dbo.Usuario` (idUsu)
