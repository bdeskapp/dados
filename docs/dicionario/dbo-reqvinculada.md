---
gerado: sincronizacao
---

# dbo.ReqVinculada

**Selo:** Explicada

Explicada em:

- [vínculos entre requisições](../fatos/vinculos.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idReqVinculo` | INT | não | sim | não |
| `idTpVinculo` | INT | não | não | não |
| `idFlu` | INT | sim | não | não |
| `nivel` | SMALLINT | sim | não | não |
| `cdVinc` | CHAR(5) | sim | não | não |
| `idFluNotNull` | computada | sim | não | sim |

## Chaves estrangeiras

- `dbo.ReqVinculada` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqVinculada` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.ReqVinculada` (cdVinc) → `dbo.Vinculo` (cdVinc)
