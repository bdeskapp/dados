---
gerado: sincronizacao
---

# dbo.ASKCode

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `type` | CHAR(1) | não | sim | não |
| `date` | DATETIME | não | sim | não |
| `code` | VARCHAR(100) | não | não | não |

## Chaves estrangeiras

- `dbo.ASKCode` (idUsu) → `dbo.Usuario` (idUsu)
