---
gerado: sincronizacao
---

# dbo.NotificacaoDocUsu

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNotDoc` | INT | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idExt` | INT | sim | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `flgLida` | BIT | não | não | não |
| `dsErro` | VARCHAR(500) | sim | não | não |
| `emailErro` | VARCHAR(100) | sim | não | não |
| `dtErro` | DATETIME | sim | não | não |
| `nTentativa` | TINYINT | sim | não | não |
| `email` | VARCHAR(100) | sim | não | não |

## Chaves estrangeiras

- `dbo.NotificacaoDocUsu` (idNotDoc) → `dbo.NotificacaoDoc` (idNotDoc)
- `dbo.NotificacaoDocUsu` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.NotificacaoDocUsu` (idExt) → `dbo.UsuarioExterno` (idExt)
