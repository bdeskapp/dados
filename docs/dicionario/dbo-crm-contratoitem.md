---
gerado: sincronizacao
---

# dbo.CRM_ContratoItem

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idItemContrato` | INT | não | sim | não |
| `idContrato` | INT | não | não | não |
| `nuItem` | SMALLINT | não | não | não |
| `tpFormato` | CHAR(1) | sim | não | não |
| `dsItem` | VARCHAR(100) | não | não | não |
| `dtIniVigencia` | DATETIME | não | não | não |
| `dtFimVigencia` | DATETIME | sim | não | não |
| `idEmpEmissorNF` | INT | sim | não | não |
| `nuHTMin` | SMALLINT | sim | não | não |
| `valTotal` | MONEY | sim | não | não |
| `valHT` | MONEY | sim | não | não |
| `valHE` | MONEY | sim | não | não |
| `nuPrcHE` | DECIMAL(5,2) | sim | não | não |
| `nuPrcNoturno` | DECIMAL(5,2) | sim | não | não |
| `nuPrcSab` | DECIMAL(5,2) | sim | não | não |
| `nuPrcDom` | DECIMAL(5,2) | sim | não | não |
| `idCan` | INT | sim | não | não |
| `dsObs` | TEXT | sim | não | não |
| `idProd` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_ApontCalc` (idItemContrato) → `dbo.CRM_ContratoItem` (idItemContrato)
- `dbo.CRM_ContratoItem` (idContrato) → `dbo.CRM_Contrato` (idContrato)
- `dbo.CRM_ContratoItem` (idProd) → `dbo.CRM_Produto` (idProd)
- `dbo.CRM_ContratoItem` (idCan) → `dbo.CalendarioNome` (idCan)
- `dbo.CRM_ContratoItem` (idEmpEmissorNF) → `dbo.Empresa` (idEmp)
- `dbo.CRM_Faturamento` (idItemContrato) → `dbo.CRM_ContratoItem` (idItemContrato)
