---
gerado: sincronizacao
---

# dbo.ListaIC

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idListaIC` | INT | não | sim | não |
| `dsListaIC` | VARCHAR(50) | não | não | não |
| `idUsuCreate` | INT | não | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `idUsuChange` | INT | sim | não | não |
| `dtChange` | DATETIME | sim | não | não |
| `flgListaICAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelRelacionado` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICClasseTipo` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICListaAdminitrador` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICListaAdminitrador` (idListaICAdm) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICUsuario` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaIC` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ListaIC` (idUsuChange) → `dbo.Usuario` (idUsu)
