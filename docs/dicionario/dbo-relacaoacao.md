---
gerado: sincronizacao
---

# dbo.RelacaoAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `dsHistorico` | VARCHAR(1000) | sim | não | não |
| `idMotivo` | INT | sim | não | não |
| `idFrmPapelDestino` | INT | sim | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |
| `idPart` | INT | sim | não | não |
| `idRotinaOrigem` | INT | sim | não | não |
| `idFrmPapelOrigem` | INT | sim | não | não |
| `nDInicio` | TINYINT | sim | não | não |
| `nDFim` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.RelacaoAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.RelacaoAcao` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.RelacaoAcao` (idFrmPapelOrigem) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAcao` (idFrmPapelDestino) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAcao` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.RelacaoAcao` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoAcao` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
