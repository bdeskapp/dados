---
gerado: sincronizacao
---

# dbo.LicDistrib

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idHie` | INT | não | sim | não |
| `qtdAloc` | INT | não | não | não |
| `qtdUso` | INT | não | não | não |
| `qtdReserva` | INT | não | não | não |
| `qtdDisp` | computada | sim | não | sim |

## Chaves estrangeiras

- `dbo.LicDistrib` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicDistrib` (idPat) → `dbo.Patrimonio` (idPat)
