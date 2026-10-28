---
gerado: sincronizacao
---

# dbo.ReqMsgAcessoConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqMsg` | INT | não | sim | não |
| `idReqPart` | INT | não | sim | não |
| `dtInicio` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqMsgAcessoConcluida` (idReqMsg) → `dbo.ReqMsgConcluida` (idReqMsg)
- `dbo.ReqMsgAcessoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
