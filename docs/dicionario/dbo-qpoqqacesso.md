---
gerado: sincronizacao
---

# dbo.QPOQQAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQPOQQ` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.QPOQQAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.QPOQQAcesso` (idQPOQQ) → `dbo.QPOQQ` (idQpoqq)
