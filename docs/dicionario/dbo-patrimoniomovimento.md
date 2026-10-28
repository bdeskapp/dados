---
gerado: sincronizacao
---

# dbo.PatrimonioMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `qtdPatMov` | INT | sim | não | não |
| `idPatMov` | INT | não | sim | não |
| `idTpPatMov` | INT | sim | não | não |
| `dtPatMov` | DATETIME | sim | não | não |
| `dsNFiscal` | VARCHAR(20) | sim | não | não |
| `nmFornecedor` | VARCHAR(20) | sim | não | não |
| `dsObsLicMov` | CHAR(250) | sim | não | não |
| `dtPatRenov` | DATETIME | sim | não | não |
| `qtdDiasAbrirOS` | INT | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `idOs` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `idUsuSolic` | INT | sim | não | não |
| `idStatusPatAnterior` | INT | sim | não | não |
| `idStatusPatNovo` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idARE` | INT | sim | não | não |
| `idLocDest` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.PatrimonioMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
- `dbo.PatrimonioMovimento` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioMovimento` (idPat) → `dbo.Patrimonio` (idPat)
