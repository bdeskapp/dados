---
gerado: sincronizacao
---

# dbo.PastaReq

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPasta` | INT | não | sim | não |
| `idReq` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.PastaReq` (idPasta) → `dbo.Pasta` (idPasta)
