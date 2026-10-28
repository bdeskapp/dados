---
gerado: sincronizacao
---

# dbo.UsuarioGrupo

**Selo:** Explicada

Explicada em:

- [grupo e área](../dimensoes/grupo-area.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `tpAlerta` | TINYINT | não | não | não |
| `nivelAlerta` | TINYINT | não | não | não |
| `flgMailAbertura` | BIT | não | não | não |
| `flgMailLiberacaoWF` | BIT | não | não | não |
| `flgMntOSReg` | TINYINT | sim | não | não |
| `flgMntOSDir` | TINYINT | sim | não | não |
| `flgMntOSFlu` | TINYINT | sim | não | não |
| `flgMntOSResumo` | TINYINT | sim | não | não |
| `flgMntOSVip` | TINYINT | sim | não | não |
| `flgAssume` | BIT | não | não | não |
| `flgAtribui` | BIT | não | não | não |
| `flgRecebeNot` | BIT | não | não | não |
| `flgAdministra` | BIT | não | não | não |
| `flgRecebeSMS` | BIT | não | não | não |
| `flgLembrete` | INT | sim | não | não |
| `idTpEsc` | INT | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioGrupo` (idGru) → `dbo.Grupo` (idGru)
- `dbo.UsuarioGrupo` (idTpEsc) → `dbo.TipoEscalonamento` (idTpEsc)
- `dbo.UsuarioGrupo` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioGrupo` (idUsuOperacao) → `dbo.Usuario` (idUsu)
