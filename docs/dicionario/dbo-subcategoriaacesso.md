---
gerado: sincronizacao
---

# dbo.SubCategoriaAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSca` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `prcSLA` | SMALLINT | sim | não | não |
| `tpSla` | CHAR(1) | não | não | não |
| `Sla` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.SubCategoriaAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.SubCategoriaAcesso` (idSca) → `dbo.SubCategoria` (idSca)
