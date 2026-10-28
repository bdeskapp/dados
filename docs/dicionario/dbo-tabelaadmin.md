---
gerado: sincronizacao
---

# dbo.TabelaAdmin

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTab` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtIni` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.TabelaAdmin` (idTab) → `dbo.Tabela` (idTab)
- `dbo.TabelaAdmin` (idUsu) → `dbo.Usuario` (idUsu)
