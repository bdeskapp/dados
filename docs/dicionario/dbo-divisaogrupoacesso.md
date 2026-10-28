---
gerado: sincronizacao
---

# dbo.DivisaoGrupoAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDiv` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DivisaoGrupoAcesso` (idDiv) → `dbo.Divisao` (idDiv)
- `dbo.DivisaoGrupoAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
