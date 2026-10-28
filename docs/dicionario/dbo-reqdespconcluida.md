---
gerado: sincronizacao
---

# dbo.ReqDespConcluida

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqDesp` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `nmUsu` | VARCHAR(100) | não | não | não |
| `dtDespesa` | DATETIME | não | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `idCatDesp` | INT | não | não | não |
| `dsCatDesp` | VARCHAR(30) | não | não | não |
| `idItemDesp` | INT | não | não | não |
| `dsItemDesp` | VARCHAR(30) | não | não | não |
| `idFornecedor` | INT | sim | não | não |
| `RazaoSocial` | VARCHAR(50) | sim | não | não |
| `valDespesa` | MONEY | não | não | não |
| `nuDoc` | VARCHAR(10) | sim | não | não |
| `dsDespesa` | VARCHAR(100) | sim | não | não |
| `obsReporte` | VARCHAR(1000) | sim | não | não |
| `flgFatura` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqDespConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
- `dbo.ReqDespConcluida` (idReqPart) → `dbo.ReqPartConcluida` (idReqPart)
