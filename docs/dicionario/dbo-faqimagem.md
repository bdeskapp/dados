---
gerado: sincronizacao
---

# dbo.FAQImagem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idImg` | INT | não | sim | não |
| `cdImg` | INT | sim | não | não |
| `dsVersao` | VARCHAR(50) | sim | não | não |
| `dsImg` | VARCHAR(50) | não | não | não |
| `dsArquivo` | VARCHAR(255) | não | não | não |
| `flgSistema` | BIT | não | não | não |
| `idFAQ` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FAQImagem` (idFAQ) → `dbo.FAQ` (idFAQ)
