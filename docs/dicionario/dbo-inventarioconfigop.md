---
gerado: sincronizacao
---

# dbo.InventarioConfigOp

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpp` | INT | não | sim | não |
| `idPatOpEntrada` | INT | sim | não | não |
| `idPatOpAjuste` | INT | sim | não | não |
| `idPatOpAssComp` | INT | sim | não | não |
| `idPatOpDissComp` | INT | sim | não | não |
| `idPatOpAssSoft` | INT | sim | não | não |
| `idPatOpDissSoft` | INT | sim | não | não |
| `idPatOpAssMon` | INT | sim | não | não |
| `idPatOpDissMon` | INT | sim | não | não |
| `flgListaDiv` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.InventarioConfigOp` (idPatOpAjuste) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssComp) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssMon) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssSoft) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissComp) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissMon) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissSoft) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpEntrada) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
