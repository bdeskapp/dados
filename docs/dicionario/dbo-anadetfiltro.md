---
gerado: sincronizacao
---

# dbo.AnaDetFiltro

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `Classificacao` | TINYINT | não | sim | não |
| `Filtro` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.AnaDetFiltro` (idPesquisa) → `dbo.AnaPesquisa` (idPesquisa)
