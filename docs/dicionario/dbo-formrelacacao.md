---
gerado: sincronizacao
---

# dbo.FormRelacAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmRel` | INT | não | sim | não |
| `tpAcao` | CHAR(1) | não | sim | não |
| `idFrmAcao` | INT | sim | não | não |
| `dsHistorico` | VARCHAR(500) | sim | não | não |
| `idMotivo` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormRelacAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRelacAcao` (idFrmRel) → `dbo.FormRelac` (idFrmRel)
