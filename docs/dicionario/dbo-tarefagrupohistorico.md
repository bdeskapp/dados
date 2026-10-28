---
gerado: sincronizacao
---

# dbo.TarefaGrupoHistorico

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | não | não |
| `idGru` | INT | não | não | não |
| `SlaGru` | REAL | sim | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.TarefaGrupoHistorico` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupoHistorico` (idTar) → `dbo.Tarefa` (idTar)
