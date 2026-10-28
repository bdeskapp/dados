---
gerado: sincronizacao
---

# dbo.Fluxo

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlu` | INT | não | sim | não |
| `nmFlu` | VARCHAR(50) | não | não | não |
| `dsFlu` | VARCHAR(255) | não | não | não |
| `flgFluAtivo` | BIT | não | não | não |
| `flgAutoAtendimento` | BIT | não | não | não |
| `idCatFlu` | INT | não | não | não |
| `flgIncompleto` | BIT | não | não | não |
| `idTpSla` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CustomFluxo` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.FluxoOS` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.FluxoTarefa` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.Fluxo` (idCatFlu) → `dbo.CategoriaFluxo` (idCatFlu)
- `dbo.Fluxo` (idTpSla) → `dbo.TipoSla` (idTpSla)
- `dbo.GrupoAcessoFluxo` (idFlu) → `dbo.Fluxo` (idFlu)
