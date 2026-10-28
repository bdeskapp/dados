---
gerado: sincronizacao
---

# dbo.RequisicaoColunaMural

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRequisicaoColunaMural` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idColuna` | INT | não | não | não |
| `flgArquivado` | BIT | não | não | não |
| `cor` | VARCHAR(7) | não | não | não |
| `posicao` | INT | não | não | não |
| `flgExcluido` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.RequisicaoColunaMural` (idColuna) → `dbo.ColunaMural` (idColuna)
