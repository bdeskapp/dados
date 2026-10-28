---
gerado: sincronizacao
---

# dbo.RepSecao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSecao` | INT | não | sim | não |
| `dsSecao` | VARCHAR(30) | não | não | não |

## Chaves estrangeiras

- `dbo.RepDetCampos` (idSecao) → `dbo.RepSecao` (idSecao)
