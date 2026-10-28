---
gerado: sincronizacao
---

# dbo.SystemCheckResult

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQQ` | INT | não | sim | não |
| `idCheck` | INT | não | sim | não |
| `dtValidacao` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.SystemCheckResult` (idCheck) → `dbo.SystemCheck` (idCheck)
