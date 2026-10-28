---
gerado: sincronizacao
---

# dbo.FormRelacStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmRel` | INT | não | não | não |
| `idFrmStatus` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormRelacStatus` (idFrmRel) → `dbo.FormRelac` (idFrmRel)
- `dbo.FormRelacStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
