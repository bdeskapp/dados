---
gerado: sincronizacao
---

# dbo.ReqPendencia

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | não | não |
| `idFrmTrans` | INT | não | não | não |
| `idReqCond` | INT | não | não | não |
| `idCond` | INT | não | não | não |
| `dsPendencia` | VARCHAR(1000) | não | não | não |
| `dtOcorr` | DATETIME | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsu` | INT | sim | não | não |
| `flgSys` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqPendencia` (idCond) → `dbo.Condicao` (idCond)
- `dbo.ReqPendencia` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.ReqPendencia` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqPendencia` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqPendencia` (idUsu) → `dbo.Usuario` (idUsu)
