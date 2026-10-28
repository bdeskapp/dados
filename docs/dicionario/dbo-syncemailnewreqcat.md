---
gerado: sincronizacao
---

# dbo.SyncEmailNewReqCat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idNewReqByEmail` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `dsKeyword` | VARCHAR(500) | não | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailNewReqCat` (idGru) → `dbo.Grupo` (idGru)
- `dbo.SyncEmailNewReqCat` (idNewReqByEmail) → `dbo.SyncEmailNewReq` (idNewReqByEmail)
- `dbo.SyncEmailNewReqCat` (idTar) → `dbo.Tarefa` (idTar)
