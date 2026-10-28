---
gerado: sincronizacao
---

# dbo.RepPesquisa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `sPesquisa` | VARCHAR(100) | sim | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `sOperCondicoes` | VARCHAR(200) | sim | não | não |
| `idEntidade` | INT | não | não | não |
| `Status` | CHAR(3) | não | não | não |
| `idUsu` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.RepDetPesquisa` (idPesquisa) → `dbo.RepPesquisa` (idPesquisa)
