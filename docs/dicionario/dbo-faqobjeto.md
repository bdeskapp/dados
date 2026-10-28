---
gerado: sincronizacao
---

# dbo.FAQObjeto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idObj` | INT | não | sim | não |
| `idFAQ` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FAQObjeto` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQObjeto` (idObj) → `dbo.Objeto` (idObj)
