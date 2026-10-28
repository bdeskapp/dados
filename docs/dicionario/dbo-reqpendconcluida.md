---
gerado: sincronizacao
---

# dbo.ReqPendConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | não | não |
| `idFrmTrans` | INT | não | não | não |
| `idCond` | INT | não | não | não |
| `dsPendencia` | VARCHAR(1000) | não | não | não |
| `dtOcorr` | DATETIME | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsu` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqPendConcluida` (idCond) → `dbo.Condicao` (idCond)
- `dbo.ReqPendConcluida` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.ReqPendConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqPendConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
- `dbo.ReqPendConcluida` (idUsu) → `dbo.Usuario` (idUsu)
