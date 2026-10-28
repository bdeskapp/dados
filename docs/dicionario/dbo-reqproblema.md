---
gerado: sincronizacao
---

# dbo.ReqProblema

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqHistCAU` | INT | sim | não | não |
| `idReqHistWKA` | INT | sim | não | não |
| `idReqHistSOL` | INT | sim | não | não |
| `idKBCAU` | INT | sim | não | não |
| `idKBWKA` | INT | sim | não | não |
| `idKBKER` | INT | sim | não | não |
| `idKBSOL` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqProblema` (idKBCAU) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBWKA) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBKER) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBSOL) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqProblema` (idReqHistCAU) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqProblema` (idReqHistWKA) → `dbo.ReqHistorico` (idReqHist)
- `dbo.ReqProblema` (idReqHistSOL) → `dbo.ReqHistorico` (idReqHist)
