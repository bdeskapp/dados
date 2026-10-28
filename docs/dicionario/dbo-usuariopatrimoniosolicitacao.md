---
gerado: sincronizacao
---

# dbo.UsuarioPatrimonioSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `idReq` | INT | não | sim | não |
| `idLoc` | INT | sim | não | não |
| `dtIniUsuPat` | DATETIME | não | não | não |
| `idPatOp` | INT | não | não | não |
| `idPatRel` | INT | sim | não | não |
| `dtValidade` | DATETIME | não | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `idStatusPat` | INT | sim | não | não |
| `idUsuSol` | INT | não | não | não |
| `tpOperacao` | CHAR(1) | não | não | não |
| `flgEfetivar` | BIT | não | não | não |
| `dsLogErro` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.UsuarioPatrimonioSolicitacao` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.UsuarioPatrimonioSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.UsuarioPatrimonioSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.UsuarioPatrimonioSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.UsuarioPatrimonioSolicitacao` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.UsuarioPatrimonioSolicitacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioPatrimonioSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
