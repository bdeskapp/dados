---
gerado: sincronizacao
---

# dbo.CRM_ApontCalc

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idSeq` | INT | não | sim | não |
| `idFat` | INT | sim | não | não |
| `idItemContrato` | INT | não | não | não |
| `qtdHT` | INT | não | não | não |
| `qtdHE` | INT | não | não | não |
| `qtdHTSab` | INT | não | não | não |
| `qtdHTDom` | INT | não | não | não |
| `qtdHTNot` | INT | não | não | não |
| `valTotHT` | MONEY | não | não | não |
| `valTotHE` | MONEY | não | não | não |
| `valTotSab` | MONEY | não | não | não |
| `valTotDom` | MONEY | não | não | não |
| `valTotNot` | MONEY | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_ApontCalc` (idItemContrato) → `dbo.CRM_ContratoItem` (idItemContrato)
- `dbo.CRM_ApontCalc` (idFat) → `dbo.CRM_Faturamento` (idFat)
