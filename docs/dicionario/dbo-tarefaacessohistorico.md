---
gerado: sincronizacao
---

# dbo.TarefaAcessoHistorico

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | não | não |
| `idGru` | INT | não | não | não |
| `prcSla` | SMALLINT | sim | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `tpSla` | CHAR(1) | não | não | não |
| `Sla` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.TarefaAcessoHistorico` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.TarefaAcessoHistorico` (idTar) → `dbo.Tarefa` (idTar)
