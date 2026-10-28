---
gerado: sincronizacao
---

# dbo.SyncEmailActionUpdate

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUpdateReqByEmail` | INT | não | sim | não |
| `idFrmAcao` | INT | não | sim | não |
| `dsKeyword` | VARCHAR(100) | não | não | não |
| `idFrmTpDoc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailActionUpdate` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.SyncEmailActionUpdate` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailActionUpdate` (idUpdateReqByEmail) → `dbo.SyncEmailUpdateReq` (idUpdateReqByEmail)
