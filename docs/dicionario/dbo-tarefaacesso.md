---
gerado: sincronizacao
---

# dbo.TarefaAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `prcSLA` | SMALLINT | sim | não | não |
| `dtEfetivo` | DATETIME | não | não | não |
| `flgPadrao` | BIT | não | não | não |
| `tpSla` | CHAR(1) | não | não | não |
| `Sla` | INT | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.TarefaAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.TarefaAcesso` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
