---
gerado: sincronizacao
---

# dbo.CondDadTabela

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idDomQQ` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CondDadTabela` (idCond) → `dbo.CondDad` (idCond)
