---
gerado: sincronizacao
---

# dbo.GrupoAcesso

**Selo:** Explicada

Explicada em:

- [grupo e área](../dimensoes/grupo-area.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `dsGru` | VARCHAR(50) | não | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |
| `flgAtivo` | BIT | não | não | não |
| `obsGru` | VARCHAR(MAX) | sim | não | não |
| `flgRestrito` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.DivisaoGrupoAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.FormAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.FormOrigemAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoFluxo` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoTipoPapel` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoUsuario` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcessoUsuario` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcesso_Categoria_ItemCardapio` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcesso_ItemCardapio` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.GrupoAcesso` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.GrupoAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Minuta` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.Patrimonio` (idGruAcesso) → `dbo.GrupoAcesso` (idGru)
- `dbo.PesqAcessoAlvo` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.PesqAcessoResult` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.QPOQQAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.RepAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.ServicoAtend` (idGruAcesso) → `dbo.GrupoAcesso` (idGru)
- `dbo.SubCategoriaAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.TarefaAcessoHistorico` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.TarefaAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
