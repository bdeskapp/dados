---
gerado: sincronizacao
---

# dbo.ListaDistrib

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLst` | INT | não | sim | não |
| `dsLst` | VARCHAR(50) | não | não | não |
| `idGruAdm` | INT | não | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `idUsuCreate` | INT | não | não | não |
| `dtAlter` | DATETIME | sim | não | não |
| `idUsuAlter` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormNotLista` (idLst) → `dbo.ListaDistrib` (idLst)
- `dbo.ListaDistribMembros` (idLst) → `dbo.ListaDistrib` (idLst)
- `dbo.ListaDistrib` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.ListaDistrib` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistrib` (idUsuAlter) → `dbo.Usuario` (idUsu)
- `dbo.ObjectSummary` (idLstRecipient) → `dbo.ListaDistrib` (idLst)
- `dbo.Tarefa` (idLstSMS) → `dbo.ListaDistrib` (idLst)
