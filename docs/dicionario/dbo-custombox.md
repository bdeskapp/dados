---
gerado: sincronizacao
---

# dbo.CustomBox

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idBox` | INT | não | sim | não |
| `idCus` | INT | não | sim | não |
| `dsBox` | VARCHAR(50) | não | não | não |

## Chaves estrangeiras

- `dbo.CustomBox` (idCus) → `dbo.Custom` (idCus)
