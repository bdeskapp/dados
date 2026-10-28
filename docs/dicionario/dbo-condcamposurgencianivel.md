---
gerado: sincronizacao
---

# dbo.CondCamposUrgenciaNivel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idUrg` | INT | não | sim | não |
| `nUrgNivel` | INT | não | sim | não |
| `idFrm` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CondCamposUrgenciaNivel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCamposUrgenciaNivel` (idUrg, nUrgNivel) → `dbo.UrgenciaNivel` (idUrg, nUrgNivel)
