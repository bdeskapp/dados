---
gerado: sincronizacao
---

# dbo.ReqDocAcessoConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDoc` | INT | não | sim | não |
| `idReqPart` | INT | não | sim | não |
| `dtInicio` | DATETIME | não | sim | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqDocAcessoConcluida` (idDoc) → `dbo.ReqDocConcluida` (idDoc)
- `dbo.ReqDocAcessoConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
