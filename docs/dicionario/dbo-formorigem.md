---
gerado: sincronizacao
---

# dbo.FormOrigem

**Selo:** Explicada

Explicada em:

- [canal e origem](../dimensoes/canal-origem.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmOrigem` | INT | não | sim | não |
| `dsFrmOrigem` | VARCHAR(30) | não | não | não |
| `idFrm` | INT | sim | não | não |
| `flgSistema` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaReq` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.CondCamposFormOrigem` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.FormOrigemAcesso` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.FormOrigem` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.LicConfig` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.Req` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
- `dbo.SyncEmailNewReq` (idFrmOrigem) → `dbo.FormOrigem` (idFrmOrigem)
