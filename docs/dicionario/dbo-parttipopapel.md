---
gerado: sincronizacao
---

# dbo.PartTipoPapel

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPTP` | INT | não | não | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `nmPart` | VARCHAR(250) | não | não | não |
| `nmPartCompleto` | VARCHAR(500) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.BubDestino` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.CondPapelPartAcao` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.CondPapelPart` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.FormPapelDominio` (idTpPapelDom, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.GrupoParticipante` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.PartTipoPapel` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.RelacaoAcao` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.RelacaoAlertaDest` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.SyncEmailNewReq` (idTpPapelAdo, idPartAdo) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.WorkflowPlan` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
