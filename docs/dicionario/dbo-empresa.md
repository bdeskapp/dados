---
gerado: sincronizacao
---

# dbo.Empresa

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEmp` | INT | não | sim | não |
| `RazaoSocial` | VARCHAR(100) | não | não | não |
| `endereco` | VARCHAR(250) | sim | não | não |
| `nmContato` | VARCHAR(50) | sim | não | não |
| `fone` | VARCHAR(20) | sim | não | não |
| `celEmp` | VARCHAR(20) | sim | não | não |
| `flgEmpAtivo` | BIT | não | não | não |
| `flgCliente` | BIT | não | não | não |
| `nmFantasia` | VARCHAR(100) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgFornecedor` | BIT | não | não | não |
| `idDiv` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_ContratoItem` (idEmpEmissorNF) → `dbo.Empresa` (idEmp)
- `dbo.CRM_Contrato` (idEmpContratada) → `dbo.Empresa` (idEmp)
- `dbo.CRM_Empresa` (idEmpCliente) → `dbo.Empresa` (idEmp)
- `dbo.EmpresaGrupoEmpresarial` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.Empresa` (idDiv) → `dbo.Divisao` (idDiv)
- `dbo.FornecedorDespesa` (idFornecedor) → `dbo.Empresa` (idEmp)
- `dbo.OS` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.ReqDespesa` (idFornecedor) → `dbo.Empresa` (idEmp)
- `dbo.Req` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.SyncUsuConfig` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.SyncUsuConfig` (idEmpHie) → `dbo.Empresa` (idEmp)
- `dbo.UsuarioHierarquia` (idEmp) → `dbo.Empresa` (idEmp)
