---
gerado: sincronizacao
---

# dbo.ReqTransTimeout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idFrmStatus` | INT | não | sim | não |
| `idFrmTrans` | INT | não | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtTimeout` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.ReqTransTimeout` (idReq) → `dbo.Req` (idReq)
