---
gerado: sincronizacao
---

# dbo.Pasta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPasta` | INT | não | sim | não |
| `idUsu` | INT | não | não | não |
| `idGru` | INT | sim | não | não |
| `dsPasta` | VARCHAR(30) | sim | não | não |

## Chaves estrangeiras

- `dbo.PastaReq` (idPasta) → `dbo.Pasta` (idPasta)
