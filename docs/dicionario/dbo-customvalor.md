---
gerado: sincronizacao
---

# dbo.CustomValor

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCus` | INT | não | sim | não |
| `idVal` | INT | não | sim | não |
| `valorCus` | VARCHAR(4000) | não | não | não |

## Chaves estrangeiras

- `dbo.CustomValor` (idCus) → `dbo.Custom` (idCus)
