---
gerado: sincronizacao
---

# dbo.RelacaoCondicao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRel` | INT | não | sim | não |
| `idCond` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RelacaoCondicao` (idCond) → `dbo.Condicao` (idCond)
- `dbo.RelacaoCondicao` (idRel) → `dbo.Relacao` (idRel)
