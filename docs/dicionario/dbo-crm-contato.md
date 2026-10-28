---
gerado: sincronizacao
---

# dbo.CRM_Contato

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CRM (contratos e faturamento)](../fora-de-escopo/crm.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idContato` | INT | não | sim | não |
| `nmContato` | VARCHAR(50) | não | não | não |
| `dsArea` | VARCHAR(50) | sim | não | não |
| `dsCargo` | VARCHAR(50) | sim | não | não |
| `nuTel` | VARCHAR(20) | sim | não | não |
| `nuCel` | VARCHAR(20) | sim | não | não |
| `email` | VARCHAR(100) | sim | não | não |
| `dsObs` | VARCHAR(1000) | sim | não | não |
| `idEmp` | INT | não | não | não |
| `idGestor` | INT | sim | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `dtExclusao` | DATETIME | sim | não | não |
| `idUsu` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_Contato` (idEmp) → `dbo.CRM_Empresa` (idEmp)
- `dbo.CRM_Contato` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.CRM_Contrato` (idContatoComercial) → `dbo.CRM_Contato` (idContato)
- `dbo.CRM_Contrato` (idContatoOperacional) → `dbo.CRM_Contato` (idContato)
