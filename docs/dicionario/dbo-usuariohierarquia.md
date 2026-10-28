---
gerado: sincronizacao
---

# dbo.UsuarioHierarquia

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idEmp` | INT | não | não | não |
| `idDir` | INT | sim | não | não |
| `idDep` | INT | sim | não | não |
| `idCoo` | INT | sim | não | não |
| `idCar` | INT | sim | não | não |
| `valorHora` | MONEY | sim | não | não |
| `idhie` | INT | sim | não | não |
| `tpUsu` | TINYINT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioHierarquia` (idCar) → `dbo.Cargo` (idCar)
- `dbo.UsuarioHierarquia` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.UsuarioHierarquia` (idhie) → `dbo.OrgHierarquia` (idHie)
- `dbo.UsuarioHierarquia` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioHierarquia` (idUsuOperacao) → `dbo.Usuario` (idUsu)
