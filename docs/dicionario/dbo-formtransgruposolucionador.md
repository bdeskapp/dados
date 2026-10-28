---
gerado: sincronizacao
---

# dbo.FormTransGrupoSolucionador

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmTrans` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormTransGrupoSolucionador` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.FormTransGrupoSolucionador` (idGru) → `dbo.Grupo` (idGru)
