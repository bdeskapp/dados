---
gerado: sincronizacao
---

# dbo.Mural

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMural` | INT | não | sim | não |
| `titulo` | VARCHAR(50) | não | não | não |
| `modo` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.ColunaMural` (idMural) → `dbo.Mural` (idMural)
- `dbo.MuralFormulario` (idMural) → `dbo.Mural` (idMural)
