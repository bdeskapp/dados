---
gerado: sincronizacao
---

# dbo.Custom

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCus` | INT | não | sim | não |
| `idTab` | INT | não | não | não |
| `nmCus` | VARCHAR(50) | não | não | não |
| `MaxLength` | INT | não | não | não |
| `dsComplementar` | VARCHAR(10) | sim | não | não |
| `Ordem` | INT | não | não | não |
| `TpCampo` | INT | não | não | não |
| `TpBox` | INT | não | não | não |
| `idCon` | INT | sim | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `flgTipoObrigatorio` | CHAR(1) | sim | não | não |
| `flgExibeLista` | BIT | sim | não | não |
| `flgExibeFiltro` | BIT | sim | não | não |

## Chaves estrangeiras

- `dbo.AgendaOSCustom` (idCus) → `dbo.Custom` (idCus)
- `dbo.CustomBox` (idCus) → `dbo.Custom` (idCus)
- `dbo.CustomValorHistorico` (idCus) → `dbo.Custom` (idCus)
- `dbo.CustomValor` (idCus) → `dbo.Custom` (idCus)
- `dbo.Custom` (idCon) → `dbo.CustomConjunto` (idCon)
- `dbo.Custom` (idTab) → `dbo.CustomTable` (idTab)
