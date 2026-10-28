---
gerado: sincronizacao
---

# dbo.CondPapel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idFrmPapel` | INT | não | não | não |
| `tpOperador` | CHAR(6) | não | não | não |

## Chaves estrangeiras

- `dbo.CondPapelPart` (idCond) → `dbo.CondPapel` (idCond)
- `dbo.CondPapel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondPapel` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
