---
gerado: sincronizacao
---

# dbo.EmpresaGrupoEmpresarial

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEmp` | INT | não | sim | não |
| `idGruEmp` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.EmpresaGrupoEmpresarial` (idGruEmp) → `dbo.CRM_GrupoEmpresarial` (idGruEmp)
- `dbo.EmpresaGrupoEmpresarial` (idEmp) → `dbo.Empresa` (idEmp)
