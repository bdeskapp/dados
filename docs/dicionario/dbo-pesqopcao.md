---
gerado: sincronizacao
---

# dbo.PesqOpcao

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOpc` | INT | não | sim | não |
| `dsOpc` | VARCHAR(100) | não | não | não |
| `idOpcConj` | INT | não | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `nPeso` | SMALLINT | não | não | não |
| `dsMotivo` | VARCHAR(2000) | sim | não | não |

## Chaves estrangeiras

- `dbo.PesqApuracaoOpc` (idOpc) → `dbo.PesqOpcao` (idOpc)
- `dbo.PesqOpcao` (idOpcConj) → `dbo.PesqOpcConjunto` (idOpcConj)
- `dbo.PesqResposta` (idOpc) → `dbo.PesqOpcao` (idOpc)
