---
gerado: sincronizacao
---

# dbo.ColunaMural

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idColuna` | INT | não | sim | não |
| `idMural` | INT | não | não | não |
| `titulo` | VARCHAR(50) | não | não | não |
| `nOrder` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ColunaMuralStatus` (idColuna) → `dbo.ColunaMural` (idColuna)
- `dbo.ColunaMural` (idMural) → `dbo.Mural` (idMural)
- `dbo.RequisicaoColunaMural` (idColuna) → `dbo.ColunaMural` (idColuna)
