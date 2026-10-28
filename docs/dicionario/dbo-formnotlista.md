---
gerado: sincronizacao
---

# dbo.FormNotLista

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmNot` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `idLst` | INT | não | não | não |
| `idFrmNotMsg` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.FormNotListaStatus` (idFrmNot) → `dbo.FormNotLista` (idFrmNot)
- `dbo.FormNotLista` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormNotLista` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.FormNotLista` (idLst) → `dbo.ListaDistrib` (idLst)
