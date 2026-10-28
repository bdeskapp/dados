---
gerado: sincronizacao
---

# dbo.FormPriMatriz

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `nImp` | TINYINT | não | sim | não |
| `nUrg` | TINYINT | não | sim | não |
| `valorPri` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPriMatriz` (idFrm) → `dbo.Formulario` (idFrm)
