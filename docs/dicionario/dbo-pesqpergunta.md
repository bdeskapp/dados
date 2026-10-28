---
gerado: sincronizacao
---

# dbo.PesqPergunta

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPergunta` | INT | não | sim | não |
| `idPesq` | INT | não | não | não |
| `dsPergunta` | VARCHAR(200) | não | não | não |
| `dsObs` | VARCHAR(MAX) | sim | não | não |
| `tpFormato` | CHAR(1) | não | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `idOpcConj` | INT | sim | não | não |
| `flgObrigatoria` | BIT | não | não | não |
| `flgComentar` | BIT | não | não | não |
| `flgAbstencao` | BIT | não | não | não |
| `tpOperadorObrigatorio` | VARCHAR(2) | sim | não | não |
| `nPesoObrigatorio` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.PesqApuracaoPerg` (idPergunta) → `dbo.PesqPergunta` (idPergunta)
- `dbo.PesqPergunta` (idOpcConj) → `dbo.PesqOpcConjunto` (idOpcConj)
- `dbo.PesqPergunta` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqResposta` (idPergunta) → `dbo.PesqPergunta` (idPergunta)
