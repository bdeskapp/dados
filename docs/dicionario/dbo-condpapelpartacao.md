---
gerado: sincronizacao
---

# dbo.CondPapelPartAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idFrmPapel` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CondPapelPartAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondPapelPartAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.CondPapelPartAcao` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
