---
gerado: sincronizacao
---

# dbo.AgendaReqPart

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAge` | INT | não | sim | não |
| `idFrmPapel` | INT | não | sim | não |
| `idTpPapel` | INT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `flgFinanceiro` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReqPart` (idAge) → `dbo.AgendaReq` (idAge)
- `dbo.AgendaReqPart` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
