---
gerado: sincronizacao
---

# dbo.ReqUltHistConcluida

**Selo:** Explicada

Explicada em:

- [eventos do histórico](../fatos/eventos-historico.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqHist` | INT | não | não | não |
| `dtUltHist` | DATETIME | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idGru` | INT | sim | não | não |
| `idReqPart` | INT | não | não | não |
| `idFrmAcao` | INT | sim | não | não |
| `dsAcao` | VARCHAR(30) | sim | não | não |
| `idMotivo` | INT | sim | não | não |
| `dsMotivo` | VARCHAR(100) | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqUltHistConcluida` (idReqHist) → `dbo.ReqHistConcluida` (idReqHist)
