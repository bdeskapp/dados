---
gerado: sincronizacao
---

# dbo.ReqVinculadaRef

**Selo:** Explicada

Explicada em:

- [vínculos entre requisições](../fatos/vinculos.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqVinculo` | INT | não | sim | não |
| `idReqPart` | INT | não | não | não |
| `cdVinc` | CHAR(5) | sim | não | não |
| `idTpVinculo` | INT | sim | não | não |
| `tpConc` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqVinculadaRef` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.ReqVinculadaRef` (cdVinc) → `dbo.Vinculo` (cdVinc)
