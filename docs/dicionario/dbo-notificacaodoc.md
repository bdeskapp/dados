---
gerado: sincronizacao
---

# dbo.NotificacaoDoc

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNotDoc` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `dsTitulo` | VARCHAR(300) | não | não | não |
| `dsNot` | TEXT | não | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `dsDocs` | VARCHAR(200) | não | não | não |

## Chaves estrangeiras

- `dbo.NotificacaoDocUsu` (idNotDoc) → `dbo.NotificacaoDoc` (idNotDoc)
