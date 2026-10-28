---
gerado: sincronizacao
---

# dbo.FormAcaoMotivo

**Selo:** Explicada

Explicada em:

- [eventos do histórico](../fatos/eventos-historico.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMotivo` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `dsMotivo` | VARCHAR(100) | não | não | não |
| `flgMotAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormAcaoMotivo` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormStatus` (idMotivoTimeout) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.RelacaoAcao` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.ReqHistorico` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.ReqRecatConcluida` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.ReqRecat` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
