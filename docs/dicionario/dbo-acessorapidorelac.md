---
gerado: sincronizacao
---

# dbo.AcessoRapidoRelac

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idObj` | INT | não | sim | não |
| `idObjRelac` | INT | não | sim | não |
| `sqOrdem` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.AcessoRapidoRelac` (idObj) → `dbo.AcessoRapido` (idObj)
- `dbo.AcessoRapidoRelac` (idObjRelac) → `dbo.AcessoRapido` (idObj)
