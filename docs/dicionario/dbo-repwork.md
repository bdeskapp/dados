---
gerado: sincronizacao
---

# dbo.RepWork

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `idEntidade` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `idSave` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RepWorkCond` (idPesquisa) → `dbo.RepWork` (idPesquisa)
- `dbo.RepWorkFields` (idPesquisa) → `dbo.RepWork` (idPesquisa)
- `dbo.RepWork` (idEntidade) → `dbo.RepEntidade` (idEntidade)
- `dbo.RepWork` (idUsu) → `dbo.Usuario` (idUsu)
