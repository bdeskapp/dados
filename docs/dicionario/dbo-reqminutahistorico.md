---
gerado: sincronizacao
---

# dbo.ReqMinutaHistorico

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqMinutaHist` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqHist` | INT | sim | não | não |
| `idMinuta` | INT | não | não | não |
| `nmMinuta` | VARCHAR(500) | não | não | não |
| `dsMinuta` | TEXT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `tpOper` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.ReqMinutaHistorico` (idMinuta) → `dbo.Minuta` (idMinuta)
- `dbo.ReqMinutaHistorico` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqMinutaHistorico` (idReqHist) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqMinutaHistorico` (idUsu) → `dbo.Usuario` (idUsu)
