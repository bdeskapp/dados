---
gerado: sincronizacao
---

# dbo.LicencaReserva

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idHie` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `qtdReservado` | INT | sim | não | não |
| `qtdAlocado` | INT | sim | não | não |
| `qtdEmUso` | NUMERIC(9,0) | sim | não | não |

## Chaves estrangeiras

- `dbo.LicencaReserva` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReserva` (idPat) → `dbo.Patrimonio` (idPat)
