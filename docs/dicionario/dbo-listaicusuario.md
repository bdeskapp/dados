---
gerado: sincronizacao
---

# dbo.ListaICUsuario

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idListaIC` | INT | não | sim | não |
| `idPat` | INT | não | sim | não |
| `idUsuAss` | INT | não | sim | não |
| `idUsuIni` | INT | não | não | não |
| `dtIni` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |
| `idUsuFim` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ListaICUsuario` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICUsuario` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.ListaICUsuario` (idUsuAss) → `dbo.Usuario` (idUsu)
- `dbo.ListaICUsuario` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICUsuario` (idUsuFim) → `dbo.Usuario` (idUsu)
