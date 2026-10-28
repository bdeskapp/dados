---
gerado: sincronizacao
---

# dbo.ReqMinuta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqHist` | INT | sim | não | não |
| `idMinuta` | INT | não | não | não |
| `nmMinuta` | VARCHAR(500) | não | não | não |
| `dsMinuta` | TEXT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqMinuta` (idMinuta) → `dbo.Minuta` (idMinuta)
- `dbo.ReqMinuta` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMinuta` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
