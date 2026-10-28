---
gerado: sincronizacao
---

# dbo.RotinaDepend

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotina` | INT | não | sim | não |
| `idPredecessora` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RotinaDepend` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.RotinaDepend` (idPredecessora) → `dbo.Rotina` (idRotina)
