---
gerado: sincronizacao
---

# dbo.SystemCheck

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCheck` | INT | não | sim | não |
| `dsCheck` | VARCHAR(500) | não | não | não |
| `dsQuery` | VARCHAR(3000) | não | não | não |
| `dsTabela` | VARCHAR(100) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.SystemCheckResult` (idCheck) → `dbo.SystemCheck` (idCheck)
