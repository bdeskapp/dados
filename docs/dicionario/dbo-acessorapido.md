---
gerado: sincronizacao
---

# dbo.AcessoRapido

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idObj` | INT | não | sim | não |
| `flgComum` | BIT | não | não | não |
| `sqOrdem` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.AcessoRapidoRelac` (idObj) → `dbo.AcessoRapido` (idObj)
- `dbo.AcessoRapidoRelac` (idObjRelac) → `dbo.AcessoRapido` (idObj)
- `dbo.AcessoRapido` (idObj) → `dbo.Objeto` (idObj)
