---
gerado: sincronizacao
---

# dbo.CondPapelAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idFrmPapel` | INT | não | sim | não |
| `tpOperador` | VARCHAR(6) | não | não | não |

## Chaves estrangeiras

- `dbo.CondPapelAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondPapelAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
