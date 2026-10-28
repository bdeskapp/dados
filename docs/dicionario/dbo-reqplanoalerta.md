---
gerado: sincronizacao
---

# dbo.ReqPlanoAlerta

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `nPerc` | INT | não | sim | não |
| `dtPrevisto` | DATETIME | não | não | não |
| `flgProcessado` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqPlanoAlerta` (idReq) → `dbo.Req` (idReq)
