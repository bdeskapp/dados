---
gerado: sincronizacao
---

# dbo.Modulo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `nmModulo` | VARCHAR(30) | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `idMod` | INT | não | sim | não |

## Chaves estrangeiras

- `ask_en_us.Objeto` (idMod) → `dbo.Modulo` (idMod)
