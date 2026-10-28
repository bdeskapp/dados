---
gerado: sincronizacao
---

# dbo.TipoVinculo

**Selo:** Explicada

Explicada em:

- [vínculos entre requisições](../fatos/vinculos.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpVinculo` | INT | não | sim | não |
| `cdTpVinculo` | CHAR(5) | não | não | não |
| `dsTpVinculo` | VARCHAR(30) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormRelac` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.ReqVinculadaRef` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.ReqVinculada` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.TipoVinculo` (cdTpVinculo) → `dbo.Vinculo` (cdVinc)
