---
gerado: sincronizacao
---

# dbo.TarefaParticipanteAprovador

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTar` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.TarefaParticipanteAprovador` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.TarefaParticipanteAprovador` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.TarefaParticipanteAprovador` (idUsuOperacao) → `dbo.Usuario` (idUsu)
