---
gerado: sincronizacao
---

# dbo.PatrimonioAssociado

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idPatAss` | INT | não | sim | não |
| `dtIniPatAss` | DATETIME | não | sim | não |
| `dtFimPatAss` | DATETIME | sim | não | não |
| `tpAssociacao` | CHAR(1) | não | não | não |
| `dtValAssociacao` | DATETIME | sim | não | não |
| `idPatMovIni` | INT | sim | não | não |
| `idPatMovFim` | INT | sim | não | não |
| `idPatRel` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioAssociado` (idPatMovIni) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatrimonioAssociado` (idPatMovFim) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatrimonioAssociado` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAssociado` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioAssociado` (idPatAss) → `dbo.Patrimonio` (idPat)
