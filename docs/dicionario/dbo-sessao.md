---
gerado: sincronizacao
---

# dbo.Sessao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSession` | UNIQUEIDENTIFIER | não | sim | não |
| `idUsu` | INT | não | não | não |
| `dtLogin` | DATETIME | não | não | não |
| `dtAcesso` | DATETIME | sim | não | não |
| `idReq` | INT | sim | não | não |
| `idObj` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.Sessao` (idUsu) → `dbo.Usuario` (idUsu)
