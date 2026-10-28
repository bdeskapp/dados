---
gerado: sincronizacao
---

# dbo.Patrimonio

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idTpp` | INT | não | não | não |
| `nmPat` | VARCHAR(50) | sim | não | não |
| `numero` | VARCHAR(30) | sim | não | não |
| `dsPat` | VARCHAR(250) | sim | não | não |
| `idLoc` | INT | sim | não | não |
| `idMar` | INT | sim | não | não |
| `serie` | VARCHAR(30) | sim | não | não |
| `dtIniPat` | DATETIME | não | não | não |
| `dtFimPat` | DATETIME | sim | não | não |
| `flgAluguel` | BIT | não | não | não |
| `flgPatAtivo` | BIT | não | não | não |
| `dtGarantia` | DATETIME | sim | não | não |
| `idStatusPat` | INT | sim | não | não |
| `dsVersao` | VARCHAR(20) | sim | não | não |
| `idHie` | INT | sim | não | não |
| `idUsuResp` | INT | sim | não | não |
| `dtResp` | DATETIME | sim | não | não |
| `dtCompra` | DATETIME | sim | não | não |
| `valCompra` | MONEY | sim | não | não |
| `idGruAcesso` | INT | sim | não | não |
| `tpCriticidade` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.CompMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.ComponenteMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.DadLogPat` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.DadValorPatSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.DadValorPat` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.KBPat` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicAlerta` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicDistrib` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicReserva` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaAlerta` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaMovimento` (idPatEquip) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaReservaHieOS` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaReservaHierarquia` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicencaReserva` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.Licenca` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.ListaICUsuario` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.OS` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatAlerta` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatDocumento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatLog` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatAss) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociado` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociado` (idPatAss) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAtributoSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAtributo` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioMovimento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.Patrimonio` (idGruAcesso) → `dbo.GrupoAcesso` (idGru)
- `dbo.Patrimonio` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Patrimonio` (idMar) → `dbo.Marca` (idMar)
- `dbo.Patrimonio` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.Patrimonio` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.Patrimonio` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.Patrimonio` (idUsuResp) → `dbo.Usuario` (idUsu)
- `dbo.Req` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.UsuarioPatrimonioSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.UsuarioPatrimonio` (idPat) → `dbo.Patrimonio` (idPat)
