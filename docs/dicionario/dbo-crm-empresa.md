---
gerado: sincronizacao
---

# dbo.CRM_Empresa

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEmp` | INT | não | sim | não |
| `idSeg` | INT | sim | não | não |
| `nmEmp` | VARCHAR(100) | não | não | não |
| `dsEnd` | VARCHAR(100) | sim | não | não |
| `dsBairro` | VARCHAR(50) | sim | não | não |
| `dsCidade` | VARCHAR(50) | sim | não | não |
| `dsUF` | CHAR(2) | sim | não | não |
| `nuCEP` | CHAR(8) | sim | não | não |
| `nuTel` | VARCHAR(20) | sim | não | não |
| `dsURL` | VARCHAR(100) | sim | não | não |
| `dsRazao` | VARCHAR(100) | sim | não | não |
| `nuIE` | VARCHAR(20) | sim | não | não |
| `nuIM` | VARCHAR(20) | sim | não | não |
| `idUni` | INT | sim | não | não |
| `idGestor` | INT | sim | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `dtExclusao` | DATETIME | sim | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `idEmpCliente` | INT | sim | não | não |
| `idGruEmp` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_Contato` (idEmp) → `dbo.CRM_Empresa` (idEmp)
- `dbo.CRM_Contrato` (idEmpContratante) → `dbo.CRM_Empresa` (idEmp)
- `dbo.CRM_Empresa` (idGruEmp) → `dbo.CRM_GrupoEmpresarial` (idGruEmp)
- `dbo.CRM_Empresa` (idSeg) → `dbo.CRM_Segmento` (idSeg)
- `dbo.CRM_Empresa` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_Empresa` (idEmpCliente) → `dbo.Empresa` (idEmp)
