---
gerado: sincronizacao
---

# dbo.UrgenciaNivel

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUrg` | INT | não | sim | não |
| `nUrgNivel` | INT | não | sim | não |
| `dsUrgNivel` | VARCHAR(50) | não | não | não |

## Chaves estrangeiras

- `dbo.CondCamposUrgenciaNivel` (idUrg, nUrgNivel) → `dbo.UrgenciaNivel` (idUrg, nUrgNivel)
- `dbo.UrgenciaNivel` (idUrg) → `dbo.Urgencia` (idUrg)
