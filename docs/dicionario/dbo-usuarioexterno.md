---
gerado: sincronizacao
---

# dbo.UsuarioExterno

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idExt` | INT | não | sim | não |
| `idAre` | INT | não | não | não |
| `email` | VARCHAR(100) | sim | não | não |
| `nmExt` | VARCHAR(100) | não | não | não |
| `nmEmp` | VARCHAR(100) | sim | não | não |
| `nuTel` | VARCHAR(20) | sim | não | não |
| `nuCel` | VARCHAR(20) | sim | não | não |
| `cdExt` | VARCHAR(20) | sim | não | não |
| `dsObs` | VARCHAR(4000) | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `flgAtivo` | BIT | não | não | não |
| `tpCod` | CHAR(1) | sim | não | não |
| `Endereco` | VARCHAR(100) | sim | não | não |
| `Bairro` | VARCHAR(50) | sim | não | não |
| `Cidade` | VARCHAR(50) | sim | não | não |
| `UF` | VARCHAR(50) | sim | não | não |
| `CEP` | VARCHAR(20) | sim | não | não |
| `Pais` | VARCHAR(50) | sim | não | não |
| `nuCel2` | VARCHAR(20) | sim | não | não |

## Chaves estrangeiras

- `dbo.NotificacaoDocUsu` (idExt) → `dbo.UsuarioExterno` (idExt)
- `dbo.NotificacaoExt` (idUsu) → `dbo.UsuarioExterno` (idExt)
- `dbo.UsuarioExterno` (idAre) → `dbo.Area` (idAre)
