---
gerado: sincronizacao
---

# dbo.OrgHierarquia

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idHie` | INT | não | sim | não |
| `idNiv` | INT | não | não | não |
| `dsHie` | VARCHAR(100) | sim | não | não |
| `sigla` | VARCHAR(5) | sim | não | não |
| `idHieAsc` | INT | sim | não | não |
| `idEmp` | INT | não | não | não |
| `ccustoHie` | VARCHAR(1000) | sim | não | não |
| `dtIniHie` | DATETIME | não | não | não |
| `dtFimHie` | DATETIME | sim | não | não |
| `idUsuResponsavel` | INT | sim | não | não |
| `dsHieComp` | VARCHAR(1200) | sim | não | não |

## Chaves estrangeiras

- `dbo.LicDistrib` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicReserva` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaMovimento` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHieOS` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHierarquia` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReservaHierarquia` (idHieAsc) → `dbo.OrgHierarquia` (idHie)
- `dbo.LicencaReserva` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.MetricaCalc_Hie` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.OS` (idhie) → `dbo.OrgHierarquia` (idHie)
- `dbo.OrgHierarquia` (idHieAsc) → `dbo.OrgHierarquia` (idHie)
- `dbo.OrgHierarquia` (idNiv) → `dbo.OrgNivel` (idNiv)
- `dbo.OrgHierarquia` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
- `dbo.Patrimonio` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.RegistroLigacao` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.Req` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.UsuarioHierarquia` (idhie) → `dbo.OrgHierarquia` (idHie)
