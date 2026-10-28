---
gerado: sincronizacao
---

# dbo.CondStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `tpOperador` | CHAR(6) | não | não | não |
| `idFrmStatus` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CondStatus` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
