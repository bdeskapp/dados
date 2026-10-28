---
gerado: sincronizacao
---

# dbo.TransicaoCondicional

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotTran` | INT | não | sim | não |
| `idRotina` | INT | não | sim | não |
| `idCond` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.TransicaoCondicional` (idCond) → `dbo.Condicao` (idCond)
- `dbo.TransicaoCondicional` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.TransicaoCondicional` (idRotTran) → `dbo.RotinaTransicao` (idRotTran)
