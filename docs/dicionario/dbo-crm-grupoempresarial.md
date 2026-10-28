---
gerado: sincronizacao
---

# dbo.CRM_GrupoEmpresarial

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGruEmp` | INT | não | sim | não |
| `dsGruEmp` | VARCHAR(100) | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_Empresa` (idGruEmp) → `dbo.CRM_GrupoEmpresarial` (idGruEmp)
- `dbo.EmpresaGrupoEmpresarial` (idGruEmp) → `dbo.CRM_GrupoEmpresarial` (idGruEmp)
