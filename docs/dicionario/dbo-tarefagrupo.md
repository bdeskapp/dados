---
gerado: sincronizacao
---

# dbo.TarefaGrupo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `SlaGru` | REAL | sim | não | não |
| `flgSomenteConsulta` | BIT | não | não | não |
| `dsOpCond` | VARCHAR(200) | sim | não | não |
| `dtEfetivo` | DATETIME | não | não | não |
| `flgRequerApontamento` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.TarefaGrupo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.TarefaGrupo` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaGrupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
