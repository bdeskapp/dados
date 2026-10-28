---
gerado: sincronizacao
---

# dbo.LicReserva

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idHie` | INT | não | sim | não |
| `idReq` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.LicReserva` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicReserva` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicReserva` (idReq) → `dbo.Req` (idReq)
- `dbo.LicReserva` (idUsu) → `dbo.Usuario` (idUsu)
