---
gerado: sincronizacao
---

# dbo.UsuarioPatrimonio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `dtIniUsuPat` | DATETIME | não | sim | não |
| `dtFimUsuPat` | DATETIME | sim | não | não |
| `tpAssociacao` | CHAR(1) | sim | não | não |
| `dtValAssociacao` | DATETIME | sim | não | não |
| `idPatMovIni` | INT | sim | não | não |
| `idPatMovFim` | INT | sim | não | não |
| `idPatRel` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioPatrimonio` (idPatMovIni) → `dbo.PatMovimento` (idPatMov)
- `dbo.UsuarioPatrimonio` (idPatMovFim) → `dbo.PatMovimento` (idPatMov)
- `dbo.UsuarioPatrimonio` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.UsuarioPatrimonio` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.UsuarioPatrimonio` (idUsu) → `dbo.Usuario` (idUsu)
