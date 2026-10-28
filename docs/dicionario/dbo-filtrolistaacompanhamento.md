---
gerado: sincronizacao
---

# dbo.FiltroListaAcompanhamento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFiltro` | INT | não | sim | não |
| `dsFiltro` | VARCHAR(100) | não | não | não |
| `sFiltroJSON` | TEXT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtCriado` | DATETIME | não | não | não |
| `flgFiltroListaAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FiltroListaAcompanhamento` (idUsu) → `dbo.Usuario` (idUsu)
