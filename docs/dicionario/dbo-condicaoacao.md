---
gerado: sincronizacao
---

# dbo.CondicaoAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `tpCondicao` | CHAR(1) | não | não | não |
| `idFrmAcao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CondDadAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondDadDominioAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondPapelAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondPapelPartAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondTarefaAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondicaoAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
