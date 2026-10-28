---
gerado: sincronizacao
---

# dbo.CompMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCompMov` | INT | não | sim | não |
| `idAtr` | INT | não | não | não |
| `dtMov` | DATETIME | não | não | não |
| `idPatOp` | INT | não | não | não |
| `qtdMov` | INT | não | não | não |
| `idUsuResp` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idUsuMov` | INT | sim | não | não |
| `idPat` | INT | sim | não | não |
| `idReq` | INT | sim | não | não |
| `idLocE` | INT | sim | não | não |
| `idStatusE` | INT | sim | não | não |
| `idLocS` | INT | sim | não | não |
| `idStatusS` | INT | sim | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `dtValAss` | DATETIME | sim | não | não |
| `flgProrrogacao` | BIT | sim | não | não |
| `flgInventario` | BIT | não | não | não |
| `flgDireto` | BIT | não | não | não |
| `idReqNConforme` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CompMovCompl` (idCompMov) → `dbo.CompMovimento` (idCompMov)
- `dbo.CompMovimento` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.CompMovimento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.CompMovimento` (idLocE) → `dbo.Localiza` (idLoc)
- `dbo.CompMovimento` (idLocS) → `dbo.Localiza` (idLoc)
- `dbo.CompMovimento` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.CompMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.CompMovimento` (idStatusE) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.CompMovimento` (idStatusS) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.CompMovimento` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.CompMovimento` (idUsuMov) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAtributo` (idCompMovIni) → `dbo.CompMovimento` (idCompMov)
- `dbo.PatrimonioAtributo` (idCompMovFim) → `dbo.CompMovimento` (idCompMov)
- `dbo.PatrimonioAtributo` (idCompMovAlt) → `dbo.CompMovimento` (idCompMov)
