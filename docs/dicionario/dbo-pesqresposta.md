---
gerado: sincronizacao
---

# dbo.PesqResposta

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idResp` | INT | não | sim | não |
| `idPergunta` | INT | não | sim | não |
| `idOpc` | INT | sim | não | não |
| `dsResposta` | VARCHAR(8000) | sim | não | não |
| `flgAbstencao` | BIT | sim | não | não |
| `dsMotivo` | VARCHAR(2000) | sim | não | não |

## Chaves estrangeiras

- `dbo.PesqResposta` (idOpc) → `dbo.PesqOpcao` (idOpc)
- `dbo.PesqResposta` (idPergunta) → `dbo.PesqPergunta` (idPergunta)
- `dbo.PesqResposta` (idResp) → `dbo.PesqRespCab` (idResp)
