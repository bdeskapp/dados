---
gerado: sincronizacao
---

# dbo.StatusPatrimonio

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idStatusPat` | INT | não | sim | não |
| `flgIncrInventario` | SMALLINT | não | não | não |
| `flgStatusPatAtivo` | SMALLINT | não | não | não |
| `dsStatusPat` | VARCHAR(100) | sim | não | não |
| `idClas` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CompEstoque` (idStatus) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.CompMovimento` (idStatusE) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.CompMovimento` (idStatusS) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.ComponenteLocal` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.ComponenteMovimento` (idStatusPatAnterior) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.ComponenteMovimento` (idStatusPatNovo) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatMovimento` (idStatusAnt) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatMovimento` (idStatusAtual) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatOperacao` (idStatus) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAssociadoSolicitacao` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAtributoSolicitacao` (idStatusE) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatrimonioAtributoSolicitacao` (idStatusS) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.Patrimonio` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.StatusPatrimonio` (idClas) → `dbo.Classe` (idClas)
- `dbo.UsuarioPatrimonioSolicitacao` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
