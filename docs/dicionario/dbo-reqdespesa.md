---
gerado: sincronizacao
---

# dbo.ReqDespesa

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqDesp` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtDespesa` | DATETIME | não | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `idCatDesp` | INT | não | não | não |
| `idItemDesp` | INT | não | não | não |
| `idFornecedor` | INT | sim | não | não |
| `valDespesa` | MONEY | não | não | não |
| `nuDoc` | VARCHAR(10) | sim | não | não |
| `dsDespesa` | VARCHAR(100) | sim | não | não |
| `obsReporte` | VARCHAR(1000) | sim | não | não |
| `flgFatura` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.ReqDespesa` (idFornecedor) → `dbo.Empresa` (idEmp)
- `dbo.ReqDespesa` (idItemDesp) → `dbo.ItemDespesa` (idItemDesp)
- `dbo.ReqDespesa` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqDespesa` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqDespesa` (idUsu) → `dbo.Usuario` (idUsu)
