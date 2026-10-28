---
gerado: sincronizacao
---

# dbo.PatrimonioAtributoSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAtr` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `idReq` | INT | não | sim | não |
| `idPatOp` | INT | não | não | não |
| `qtdMov` | INT | não | não | não |
| `idUsuResp` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idLocE` | INT | sim | não | não |
| `idStatusE` | INT | sim | não | não |
| `idLocS` | INT | sim | não | não |
| `idStatusS` | INT | sim | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `tpAssociacao` | CHAR(1) | não | não | não |
| `idPatRel` | INT | sim | não | não |
| `dtValidade` | DATETIME | sim | não | não |
| `bDefinitivo` | BIT | não | não | não |
| `bAfetaEstoque` | BIT | não | não | não |
| `idUsuSol` | INT | sim | não | não |
| `dtSolicitacao` | DATETIME | não | não | não |
| `tpOperacao` | CHAR(1) | não | não | não |
| `flgEfetivar` | BIT | não | não | não |
| `dsLogErro` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioAtributoSolicitacao` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.PatrimonioAtributoSolicitacao` (idGru) → `dbo.Grupo` (idGru)
- `dbo.PatrimonioAtributoSolicitacao` (idLocE) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAtributoSolicitacao` (idLocS) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAtributoSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatrimonioAtributoSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAtributoSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAtributoSolicitacao` (idStatusE) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAtributoSolicitacao` (idStatusS) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAtributoSolicitacao` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAtributoSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
