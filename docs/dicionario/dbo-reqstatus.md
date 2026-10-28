---
gerado: sincronizacao
---

# dbo.ReqStatus

**Selo:** Explicada

Explicada em:

- [tempo por status](../fatos/tempo-por-status.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqStatus` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idFrmStatus` | INT | não | não | não |
| `dtIniStatus` | DATETIME | não | não | não |
| `dtFimStatus` | DATETIME | sim | não | não |
| `nIntervaloReal` | INT | sim | não | não |
| `nIntervaloCal` | INT | sim | não | não |
| `flgUtilizado` | BIT | não | não | não |
| `dtUltimoAlerta` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ReqStatus` (idReq) → `dbo.Req` (idReq)
