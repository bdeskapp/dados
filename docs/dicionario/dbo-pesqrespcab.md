---
gerado: sincronizacao
---

# dbo.PesqRespCab

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idResp` | INT | não | sim | não |
| `idPesq` | INT | não | não | não |
| `dtResp` | DATETIME | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idReq` | INT | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `idProc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.PesqRespCab` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqResposta` (idResp) → `dbo.PesqRespCab` (idResp)
