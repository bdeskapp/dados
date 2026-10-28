---
gerado: sincronizacao
---

# dbo.PatOpQPOQQ

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQpoqq` | INT | não | sim | não |
| `idPatOp` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.PatOpQPOQQ` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatOpQPOQQ` (idQpoqq) → `dbo.QPOQQ` (idQpoqq)
