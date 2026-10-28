---
gerado: sincronizacao
---

# dbo.CondCamposFormOrigem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idFrmOrigem` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CondCamposFormOrigem` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCamposFormOrigem` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
