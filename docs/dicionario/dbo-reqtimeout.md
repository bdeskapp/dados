---
gerado: sincronizacao
---

# dbo.ReqTimeout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idCausa` | INT | não | sim | não |
| `idFrmStatus` | INT | não | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtTimeout` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.ReqTimeout` (idCausa) → `dbo.Causa` (idCausa)
- `dbo.ReqTimeout` (idReq) → `dbo.Req` (idReq)
