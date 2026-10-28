---
gerado: sincronizacao
---

# dbo.ColunaMuralStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idColuna` | INT | não | sim | não |
| `idFrmStatus` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.ColunaMuralStatus` (idColuna) → `dbo.ColunaMural` (idColuna)
- `dbo.ColunaMuralStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
