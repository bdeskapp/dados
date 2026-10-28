---
gerado: sincronizacao
---

# dbo.FormTransTimeout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmTrans` | INT | não | sim | não |
| `prcTimeout` | SMALLINT | sim | não | não |
| `valTimeout` | INT | sim | não | não |
| `dsHistorico` | VARCHAR(250) | sim | não | não |
| `idMotivo` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormTransTimeout` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
