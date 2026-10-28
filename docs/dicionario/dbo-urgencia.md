---
gerado: sincronizacao
---

# dbo.Urgencia

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUrg` | INT | não | sim | não |
| `dsUrg` | VARCHAR(50) | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `dsHelp` | TEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPri` (idUrg) → `dbo.Urgencia` (idUrg)
- `dbo.UrgenciaNivel` (idUrg) → `dbo.Urgencia` (idUrg)
