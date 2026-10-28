---
gerado: sincronizacao
---

# dbo.KBPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idKBPat` | INT | não | sim | não |
| `idKB` | INT | não | não | não |
| `idTpp` | INT | não | não | não |
| `idMar` | INT | não | não | não |
| `idPat` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.KBPat` (idKB) → `dbo.KBase` (idKB)
- `dbo.KBPat` (idMar) → `dbo.Marca` (idMar)
- `dbo.KBPat` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.KBPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
