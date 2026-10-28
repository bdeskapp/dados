---
gerado: sincronizacao
---

# dbo.KBase

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [base de conhecimento](../fora-de-escopo/base-de-conhecimento.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idKB` | INT | não | sim | não |
| `nmKB` | VARCHAR(150) | sim | não | não |
| `dsKB` | TEXT | não | não | não |
| `flgKBAtivo` | BIT | não | não | não |
| `dtCriacao` | DATETIME | sim | não | não |
| `dtAtualizacao` | DATETIME | sim | não | não |
| `idAutor` | INT | sim | não | não |
| `idRevisor` | INT | sim | não | não |
| `flgTpKB` | TINYINT | não | não | não |
| `cdKB` | VARCHAR(15) | sim | não | não |
| `idReqOrigem` | INT | sim | não | não |
| `idAre` | INT | sim | não | não |
| `idGruResp` | INT | sim | não | não |
| `tpAcesso` | TINYINT | sim | não | não |
| `cdKBClas` | CHAR(3) | sim | não | não |
| `cdKBSta` | CHAR(3) | sim | não | não |

## Chaves estrangeiras

- `dbo.AutoAtendimento` (idKb) → `dbo.KBase` (idKB)
- `dbo.KBAcesso` (idKB) → `dbo.KBase` (idKB)
- `dbo.KBPat` (idKB) → `dbo.KBase` (idKB)
- `dbo.KBRotina` (idKb) → `dbo.KBase` (idKB)
- `dbo.KBTarefa` (idKB) → `dbo.KBase` (idKB)
- `dbo.KBase` (idAre) → `dbo.Area` (idAre)
- `dbo.KBase` (idGruResp) → `dbo.Grupo` (idGru)
- `dbo.KBase` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.KBase` (idAre, cdKBClas, cdKBSta) → `dbo.KBStatus` (idAre, cdKBClas, cdKBSta)
- `dbo.KBase` (idAutor) → `dbo.Usuario` (idUsu)
- `dbo.KBase` (idRevisor) → `dbo.Usuario` (idUsu)
- `dbo.LogKB` (idKB) → `dbo.KBase` (idKB)
- `dbo.ReqKBConcluida` (idKB) → `dbo.KBase` (idKB)
- `dbo.ReqKB` (idKB) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBCAU) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBWKA) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBKER) → `dbo.KBase` (idKB)
- `dbo.ReqProblema` (idKBSOL) → `dbo.KBase` (idKB)
