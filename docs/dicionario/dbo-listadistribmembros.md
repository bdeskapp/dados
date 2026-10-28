---
gerado: sincronizacao
---

# dbo.ListaDistribMembros

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLstMembro` | INT | não | sim | não |
| `idLst` | INT | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `idUsuCreate` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ListaDistribMembros` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ListaDistribMembros` (idLst) → `dbo.ListaDistrib` (idLst)
- `dbo.ListaDistribMembros` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.ListaDistribMembros` (idUsuCreate) → `dbo.Usuario` (idUsu)
