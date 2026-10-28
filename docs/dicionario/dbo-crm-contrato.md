---
gerado: sincronizacao
---

# dbo.CRM_Contrato

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idContrato` | INT | não | sim | não |
| `nuContrato` | VARCHAR(50) | não | não | não |
| `dsTitulo` | VARCHAR(100) | sim | não | não |
| `dtIniVigencia` | DATETIME | não | não | não |
| `dtFimVigencia` | DATETIME | sim | não | não |
| `idEmpContratante` | INT | não | não | não |
| `idEmpContratada` | INT | não | não | não |
| `dsTpReajuste` | VARCHAR(30) | sim | não | não |
| `dsIndice` | VARCHAR(30) | sim | não | não |
| `idUni` | INT | não | não | não |
| `idGestor` | INT | não | não | não |
| `idContatoComercial` | INT | sim | não | não |
| `idContatoOperacional` | INT | sim | não | não |
| `idAgeRenov` | INT | sim | não | não |
| `dsObs` | TEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_ContratoDoc` (idContrato) → `dbo.CRM_Contrato` (idContrato)
- `dbo.CRM_ContratoItem` (idContrato) → `dbo.CRM_Contrato` (idContrato)
- `dbo.CRM_Contrato` (idAgeRenov) → `dbo.AgendaReq` (idAge)
- `dbo.CRM_Contrato` (idContatoComercial) → `dbo.CRM_Contato` (idContato)
- `dbo.CRM_Contrato` (idContatoOperacional) → `dbo.CRM_Contato` (idContato)
- `dbo.CRM_Contrato` (idEmpContratante) → `dbo.CRM_Empresa` (idEmp)
- `dbo.CRM_Contrato` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_Contrato` (idEmpContratada) → `dbo.Empresa` (idEmp)
