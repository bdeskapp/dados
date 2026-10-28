---
gerado: sincronizacao
---

# dbo.ObjectSummary

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdObj` | INT | não | sim | não |
| `dsTitle` | NVARCHAR(200) | não | não | não |
| `dsSubtitle` | NVARCHAR(200) | sim | não | não |
| `obsSummary` | NVARCHAR(1000) | sim | não | não |
| `nmFile` | NVARCHAR(50) | não | não | não |
| `idLstRecipient` | INT | sim | não | não |
| `cssClassLogoClientCover` | NVARCHAR(50) | não | não | não |
| `cssClassLogoASKCover` | NVARCHAR(50) | não | não | não |
| `cssClassLogoClientDetail` | NVARCHAR(50) | não | não | não |
| `cssClassLogoASKDetail` | NVARCHAR(50) | não | não | não |
| `footer` | NVARCHAR(200) | sim | não | não |
| `flgShowFooterInCover` | BIT | não | não | não |
| `idGru` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ObjectSummaryDetail` (cdObjSummary) → `dbo.ObjectSummary` (cdObj)
- `dbo.ObjectSummary` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ObjectSummary` (idLstRecipient) → `dbo.ListaDistrib` (idLst)
- `dbo.ObjectSummary` (cdObj) → `dbo.Object` (cdObj)
