---
gerado: sincronizacao
---

# dbo.FormNotListaStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmNot` | INT | não | sim | não |
| `idFrmStatus` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormNotListaStatus` (idFrmNot) → `dbo.FormNotLista` (idFrmNot)
- `dbo.FormNotListaStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
