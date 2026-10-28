---
gerado: sincronizacao
---

# dbo.FormPri

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `idImp` | INT | não | não | não |
| `idUrg` | INT | não | não | não |
| `nPesoMatriz` | TINYINT | sim | não | não |
| `nPesoAtividade` | TINYINT | sim | não | não |
| `nPesoIC` | TINYINT | sim | não | não |
| `nPriBaixa` | TINYINT | sim | não | não |
| `nPriMedia` | TINYINT | sim | não | não |
| `nPriAlta` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPri` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormPri` (idImp) → `dbo.Impacto` (idImp)
- `dbo.FormPri` (idUrg) → `dbo.Urgencia` (idUrg)
