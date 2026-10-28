---
gerado: sincronizacao
---

# dbo.TipoPapel

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpPapel` | SMALLINT | não | sim | não |
| `dsTpPapel` | VARCHAR(20) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |
| `flgUsuario` | BIT | não | não | não |
| `flgAcesso` | BIT | não | não | não |
| `corFundo` | VARCHAR(6) | sim | não | não |

## Chaves estrangeiras

- `dbo.Bub` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormPapelRelacionado` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormPapelRelacionado` (idTpPapelRelacionado) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormPapelTipo` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormPapel` (idTpPapelDefault) → `dbo.TipoPapel` (idTpPapel)
- `dbo.GrupoAcesso` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.PapelTipoPapel` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.PartTipoPapel` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.ReqPartConcluida` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.ReqParticipante` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.Tabela` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.TarefaParticipanteAprovador` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.TipoPapelDominio` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.TipoPapelDominio` (idTpPapelDom) → `dbo.TipoPapel` (idTpPapel)
