---
gerado: sincronizacao
---

# dbo.Pesquisa

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesq` | INT | não | sim | não |
| `cdPesq` | INT | não | não | não |
| `cdVersao` | SMALLINT | não | não | não |
| `dsTitulo` | VARCHAR(100) | não | não | não |
| `dsIntro` | TEXT | não | não | não |
| `dsObjetivo` | VARCHAR(500) | não | não | não |
| `dtIniVigencia` | DATETIME | não | não | não |
| `dtFimVigencia` | DATETIME | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgAnonima` | BIT | não | não | não |
| `idGru` | INT | não | não | não |
| `nmPagina` | VARCHAR(200) | sim | não | não |
| `tpPesquisa` | CHAR(1) | não | não | não |
| `tpApuracao` | CHAR(1) | não | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `nTotPrev` | INT | sim | não | não |
| `flgResponderMaisDeUmaVez` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPesquisa` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqAcessoAlvo` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqAcessoResult` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqApuracao` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqPergunta` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqRespCab` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqRespUsuario` (idPesq) → `dbo.Pesquisa` (idPesq)
