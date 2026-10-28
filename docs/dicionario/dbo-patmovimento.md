---
gerado: sincronizacao
---

# dbo.PatMovimento

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatMov` | INT | não | sim | não |
| `idPat` | INT | não | não | não |
| `dtMov` | DATETIME | não | não | não |
| `idPatOp` | INT | não | não | não |
| `idUsuResp` | INT | sim | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `idStatusAnt` | INT | sim | não | não |
| `idStatusAtual` | INT | sim | não | não |
| `idLocAnt` | INT | sim | não | não |
| `idLocAtual` | INT | sim | não | não |
| `idReq` | INT | sim | não | não |
| `flgProrrogacao` | BIT | não | não | não |
| `idUsuAss` | INT | sim | não | não |
| `idPatAss` | INT | sim | não | não |
| `dtValAss` | DATETIME | sim | não | não |
| `flgInventario` | BIT | não | não | não |
| `flgDireto` | BIT | não | não | não |
| `idReqNConforme` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadLogPat` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.LicMovimento` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatLog` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatMovimento` (idLocAnt) → `dbo.Localiza` (idLoc)
- `dbo.PatMovimento` (idLocAtual) → `dbo.Localiza` (idLoc)
- `dbo.PatMovimento` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatMovimento` (idStatusAnt) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatMovimento` (idStatusAtual) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatMovimento` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.PatrimonioAssociado` (idPatMovIni) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatrimonioAssociado` (idPatMovFim) → `dbo.PatMovimento` (idPatMov)
- `dbo.UsuarioPatrimonio` (idPatMovIni) → `dbo.PatMovimento` (idPatMov)
- `dbo.UsuarioPatrimonio` (idPatMovFim) → `dbo.PatMovimento` (idPatMov)
