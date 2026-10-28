---
gerado: sincronizacao
---

# dbo.ListaICListaAdminitrador

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idListaIC` | INT | não | sim | não |
| `idListaICAdm` | INT | não | sim | não |
| `idUsuIni` | INT | não | não | não |
| `dtIni` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |
| `idUsuFim` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ListaICListaAdminitrador` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICListaAdminitrador` (idListaICAdm) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICListaAdminitrador` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICListaAdminitrador` (idUsuFim) → `dbo.Usuario` (idUsu)
