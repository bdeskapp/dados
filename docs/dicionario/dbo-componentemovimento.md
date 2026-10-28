---
gerado: sincronizacao
---

# dbo.ComponenteMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCmpMov` | INT | não | sim | não |
| `idLoc` | INT | sim | não | não |
| `idAtr` | INT | não | não | não |
| `idTpPatMov` | INT | não | não | não |
| `dtCmpMov` | DATETIME | sim | não | não |
| `qtdCmpMov` | INT | sim | não | não |
| `nmCmpFornecedor` | VARCHAR(20) | sim | não | não |
| `dsCmpNFiscal` | VARCHAR(20) | sim | não | não |
| `dsCmpMov` | VARCHAR(250) | sim | não | não |
| `idLocDest` | INT | sim | não | não |
| `idStatusPatAnterior` | INT | sim | não | não |
| `idStatusPatNovo` | INT | sim | não | não |
| `idOs` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `idUsuSolic` | INT | sim | não | não |
| `idPat` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idARE` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ComponenteMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.ComponenteMovimento` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteMovimento` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteMovimento` (idLocDest) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.ComponenteMovimento` (idStatusPatAnterior) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.ComponenteMovimento` (idStatusPatNovo) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.ComponenteMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ComponenteMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
