---
gerado: sincronizacao
---

# dbo.Impacto

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idImp` | INT | não | sim | não |
| `dsImp` | VARCHAR(50) | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `dsHelp` | TEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPri` (idImp) → `dbo.Impacto` (idImp)
- `dbo.ImpactoNivel` (idImp) → `dbo.Impacto` (idImp)
