---
gerado: sincronizacao
---

# dbo.GerenciaGrupo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGer` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.GerenciaGrupo` (idGer) → `dbo.Gerencia` (idGer)
- `dbo.GerenciaGrupo` (idGru) → `dbo.Grupo` (idGru)
