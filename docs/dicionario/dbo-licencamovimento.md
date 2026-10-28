---
gerado: sincronizacao
---

# dbo.LicencaMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | não | não |
| `idPatEquip` | INT | sim | não | não |
| `qtdPatMov` | INT | sim | não | não |
| `idLicMov` | INT | não | sim | não |
| `idTpPatMov` | INT | sim | não | não |
| `dtPatMov` | DATETIME | sim | não | não |
| `dsNFiscal` | VARCHAR(100) | sim | não | não |
| `nmFornecedor` | VARCHAR(100) | sim | não | não |
| `dsObsLicMov` | CHAR(250) | sim | não | não |
| `dtPatRenov` | DATETIME | sim | não | não |
| `qtdDiasAbrirOS` | INT | sim | não | não |
| `idOs` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `idUsuSolic` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idHie` | INT | sim | não | não |
| `idARE` | INT | sim | não | não |
| `idLicMovAssoc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.LicencaMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.LicencaMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.LicencaMovimento` (idLicMovAssoc) → `dbo.LicencaMovimento` (idLicMov)
- `dbo.LicencaMovimento` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaMovimento` (idPatEquip) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
- `dbo.LicencaMovimento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.LicencaMovimento` (idUsuSolic) → `dbo.Usuario` (idUsu)
