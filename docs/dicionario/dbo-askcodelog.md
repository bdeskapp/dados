---
gerado: sincronizacao
---

# dbo.ASKCodeLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `dtLog` | DATETIME | não | sim | não |
| `dsLink` | VARCHAR(1000) | não | não | não |
| `dsLog` | VARCHAR(100) | não | não | não |

## Chaves estrangeiras

- `dbo.ASKCodeLog` (idUsu) → `dbo.Usuario` (idUsu)
