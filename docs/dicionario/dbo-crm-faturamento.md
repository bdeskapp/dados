---
gerado: sincronizacao
---

# dbo.CRM_Faturamento

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFat` | INT | não | sim | não |
| `dsRef` | VARCHAR(30) | não | não | não |
| `idItemContrato` | INT | não | não | não |
| `valFatTotal` | MONEY | não | não | não |
| `dtPreparo` | DATETIME | não | não | não |
| `idUsuPreparo` | INT | não | não | não |
| `dtConfirmacao` | DATETIME | sim | não | não |
| `idUsuConfirm` | INT | sim | não | não |
| `flgMinimo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_ApontCalc` (idFat) → `dbo.CRM_Faturamento` (idFat)
- `dbo.CRM_FatMemoria` (idFat) → `dbo.CRM_Faturamento` (idFat)
- `dbo.CRM_Faturamento` (idItemContrato) → `dbo.CRM_ContratoItem` (idItemContrato)
- `dbo.CRM_Faturamento` (idUsuPreparo) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Faturamento` (idUsuConfirm) → `dbo.Usuario` (idUsu)
