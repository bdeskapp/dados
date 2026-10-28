---
gerado: sincronizacao
---

# dbo.ImpactoNivel

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idImp` | INT | não | sim | não |
| `nImpNivel` | INT | não | sim | não |
| `dsImpNivel` | VARCHAR(50) | não | não | não |

## Chaves estrangeiras

- `dbo.CondCamposImpactoNivel` (idImp, nImpNivel) → `dbo.ImpactoNivel` (idImp, nImpNivel)
- `dbo.ImpactoNivel` (idImp) → `dbo.Impacto` (idImp)
