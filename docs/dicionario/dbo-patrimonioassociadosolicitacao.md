---
gerado: sincronizacao
---

# dbo.PatrimonioAssociadoSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idPatAss` | INT | não | sim | não |
| `idReq` | INT | não | sim | não |
| `dtIniPatAss` | DATETIME | não | não | não |
| `idLoc` | INT | sim | não | não |
| `idPatOp` | INT | não | não | não |
| `idPatRel` | INT | sim | não | não |
| `dtValAssociacao` | DATETIME | não | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `idStatusPat` | INT | sim | não | não |
| `idUsuAss` | INT | sim | não | não |
| `idUsuSol` | INT | não | não | não |
| `tpOperacao` | CHAR(1) | não | não | não |
| `flgEfetivar` | BIT | não | não | não |
| `dsLogErro` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioAssociadoSolicitacao` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAssociadoSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatAss) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idUsuAss) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAssociadoSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
