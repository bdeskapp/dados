---
gerado: sincronizacao
---

# dbo.LicencaReservaHieOS

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOS` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `idHie` | INT | não | sim | não |
| `idEmp` | INT | não | não | não |
| `qtdReservado` | NUMERIC(9,0) | sim | não | não |

## Chaves estrangeiras

- `dbo.LicencaReservaHieOS` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHieOS` (idPat) → `dbo.Patrimonio` (idPat)
