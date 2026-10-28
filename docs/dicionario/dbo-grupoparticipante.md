---
gerado: sincronizacao
---

# dbo.GrupoParticipante

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.GrupoParticipante` (idGru) → `dbo.Grupo` (idGru)
- `dbo.GrupoParticipante` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.GrupoParticipante` (idUsuOperacao) → `dbo.Usuario` (idUsu)
