---
gerado: sincronizacao
---

# dbo.TipoSla

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpSla` | INT | não | sim | não |
| `dsTpSla` | VARCHAR(30) | não | não | não |
| `flgTpSlaAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Fluxo` (idTpSla) → `dbo.TipoSla` (idTpSla)
