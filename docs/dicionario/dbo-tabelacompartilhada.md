---
gerado: sincronizacao
---

# dbo.TabelaCompartilhada

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTab` | INT | não | sim | não |
| `idChave` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtIni` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.TabelaCompartilhada` (idTab) → `dbo.Tabela` (idTab)
- `dbo.TabelaCompartilhada` (idUsu) → `dbo.Usuario` (idUsu)
