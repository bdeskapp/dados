---
gerado: sincronizacao
---

# dbo.FormSLA

**Selo:** Explicada

Explicada em:

- [prioridade e SLA](../dimensoes/prioridade-sla.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `cdAcao` | VARCHAR(6) | não | sim | não |
| `flgCalcDtIni` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormSLA` (idFrm) → `dbo.Formulario` (idFrm)
