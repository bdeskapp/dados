---
gerado: sincronizacao
---

# dbo.NotificacaoExt

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNot` | INT | não | sim | não |
| `idFrmNot` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `idReq` | INT | sim | não | não |
| `dsTitulo` | VARCHAR(300) | não | não | não |
| `dsNot` | TEXT | sim | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `flgLida` | BIT | não | não | não |
| `dsErro` | VARCHAR(500) | sim | não | não |
| `emailErro` | VARCHAR(100) | sim | não | não |
| `dtErro` | DATETIME | sim | não | não |
| `nTentativa` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.NotificacaoExt` (idFrmNot) → `dbo.FormNotificacao` (idFrmNot)
- `dbo.NotificacaoExt` (idUsu) → `dbo.UsuarioExterno` (idExt)
