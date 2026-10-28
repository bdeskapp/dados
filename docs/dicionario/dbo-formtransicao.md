---
gerado: sincronizacao
---

# dbo.FormTransicao

**Selo:** Explicada

Explicada em:

- [ação](../dimensoes/acao.md)
- [status](../dimensoes/status-fase.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmTrans` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `idFrmStatusAtual` | INT | sim | não | não |
| `idFrmStatusProx` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.FormTransGrupoSolucionador` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.FormTransTimeout` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.FormTransicao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormTransicao` (idFrmStatusAtual) → `dbo.FormStatus` (idFrmStatus)
- `dbo.FormTransicao` (idFrmStatusProx) → `dbo.FormStatus` (idFrmStatus)
- `dbo.ReqPendConcluida` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.ReqPendencia` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.RotinaTransicao` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
