---
gerado: sincronizacao
---

# dbo.DadDominioTabela

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idView` | INT | não | sim | não |
| `nmView` | VARCHAR(50) | não | não | não |
| `dsView` | VARCHAR(50) | não | não | não |

## Chaves estrangeiras

- `dbo.DadoAdicional` (idView) → `dbo.DadDominioTabela` (idView)
