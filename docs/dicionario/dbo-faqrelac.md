---
gerado: sincronizacao
---

# dbo.FAQRelac

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFAQ` | INT | não | sim | não |
| `idFAQRelac` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FAQRelac` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQRelac` (idFAQRelac) → `dbo.FAQ` (idFAQ)
