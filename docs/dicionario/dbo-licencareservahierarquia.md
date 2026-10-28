---
gerado: sincronizacao
---

# dbo.LicencaReservaHierarquia

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idHie` | INT | não | sim | não |
| `idEmp` | INT | não | não | não |
| `codigo` | VARCHAR(200) | sim | não | não |
| `nivel` | INT | sim | não | não |
| `qtdReservado` | NUMERIC(9,0) | sim | não | não |
| `qtdAlocado` | NUMERIC(9,0) | sim | não | não |
| `qtdEmUso` | NUMERIC(9,0) | sim | não | não |
| `idHieAsc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.LicencaReservaHierarquia` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHierarquia` (idHieAsc) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHierarquia` (idPat) → `dbo.Patrimonio` (idPat)
