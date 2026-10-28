---
gerado: sincronizacao
---

# dbo.TarefaGrupoAprovador

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.TarefaGrupoAprovador` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupoAprovador` (idTar) → `dbo.Tarefa` (idTar)
