---
gerado: sincronizacao
---

# dbo.ReqTime

**Selo:** Explicada

Explicada em:

- [tempo da requisição](../fatos/tempo-requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `dtCalc` | DATETIME | não | não | não |
| `tResp` | INT | sim | não | não |
| `tRespCal` | INT | sim | não | não |
| `tAtend` | INT | sim | não | não |
| `tAtendCal` | INT | sim | não | não |
| `tTotal` | INT | sim | não | não |
| `tTotalCal` | INT | sim | não | não |
| `tAtraso` | INT | sim | não | não |
| `tAtrasoCal` | INT | sim | não | não |
| `tFreeze` | INT | sim | não | não |
| `tFreezeCal` | INT | sim | não | não |
| `tAtivo` | INT | sim | não | não |
| `tAtivoCal` | INT | sim | não | não |
| `tAvanco` | INT | sim | não | não |
| `tAvancoCal` | INT | sim | não | não |
| `tAtrasoReal` | INT | sim | não | não |
| `tAtrasoRealCal` | INT | sim | não | não |
| `tAvancoReal` | INT | sim | não | não |
| `tAvancoRealCal` | INT | sim | não | não |
| `flgErro` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqTime` (idReq) → `dbo.Req` (idReq)
