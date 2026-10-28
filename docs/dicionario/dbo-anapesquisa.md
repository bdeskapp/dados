---
gerado: sincronizacao
---

# dbo.AnaPesquisa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `Titulo` | VARCHAR(50) | não | não | não |
| `TipoPesquisa` | TINYINT | não | não | não |
| `dtInicial` | DATETIME | não | não | não |
| `dtFinal` | DATETIME | não | não | não |
| `Classificacao` | TINYINT | não | não | não |
| `idUsu` | INT | não | não | não |
| `Acesso` | INT | não | não | não |
| `Data` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.AnaDetFiltro` (idPesquisa) → `dbo.AnaPesquisa` (idPesquisa)
- `dbo.AnaDetPesquisa` (idPesquisa) → `dbo.AnaPesquisa` (idPesquisa)
