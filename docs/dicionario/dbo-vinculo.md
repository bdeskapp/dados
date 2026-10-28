---
gerado: sincronizacao
---

# dbo.Vinculo

**Selo:** Explicada

Explicada em:

- [vínculos entre requisições](../fatos/vinculos.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdVinc` | CHAR(5) | não | sim | não |
| `dsVinc` | VARCHAR(30) | não | não | não |

## Chaves estrangeiras

- `dbo.FormRelac` (cdVinc) → `dbo.Vinculo` (cdVinc)
- `dbo.ReqVinculadaRef` (cdVinc) → `dbo.Vinculo` (cdVinc)
- `dbo.ReqVinculada` (cdVinc) → `dbo.Vinculo` (cdVinc)
- `dbo.TipoVinculo` (cdTpVinculo) → `dbo.Vinculo` (cdVinc)
