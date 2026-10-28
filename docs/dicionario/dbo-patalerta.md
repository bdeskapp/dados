---
gerado: sincronizacao
---

# dbo.PatAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatAlerta` | INT | não | sim | não |
| `idTpp` | INT | não | não | não |
| `idPat` | INT | não | não | não |
| `idPatOp` | INT | não | não | não |
| `dtOp` | DATETIME | não | não | não |
| `idUsuOp` | INT | sim | não | não |
| `idReq` | INT | sim | não | não |
| `dsNot` | TEXT | não | não | não |

## Chaves estrangeiras

- `dbo.PatAlerta` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatAlerta` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatAlerta` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.PatAlerta` (idUsuOp) → `dbo.Usuario` (idUsu)
