---
gerado: sincronizacao
---

# dbo.Favoritos

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idObj` | INT | não | sim | não |
| `idFrm` | INT | sim | não | não |
| `nSeq` | SMALLINT | não | sim | não |
| `dsFav` | VARCHAR(30) | não | não | não |
| `idProc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.Favoritos` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Favoritos` (idObj) → `dbo.Objeto` (idObj)
- `dbo.Favoritos` (idUsu) → `dbo.Usuario` (idUsu)
