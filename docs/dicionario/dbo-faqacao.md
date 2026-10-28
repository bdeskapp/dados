---
gerado: sincronizacao
---

# dbo.FAQAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAcao` | INT | não | sim | não |
| `idFAQ` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FAQAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.FAQAcao` (idFAQ) → `dbo.FAQ` (idFAQ)
