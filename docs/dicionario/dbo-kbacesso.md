---
gerado: sincronizacao
---

# dbo.KBAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idKB` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.KBAcesso` (idGru) → `dbo.Grupo` (idGru)
- `dbo.KBAcesso` (idKB) → `dbo.KBase` (idKB)
