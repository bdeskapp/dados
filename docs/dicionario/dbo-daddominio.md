---
gerado: sincronizacao
---

# dbo.DadDominio

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDom` | INT | não | sim | não |
| `idDad` | INT | não | não | não |
| `dsDom` | VARCHAR(150) | não | não | não |
| `dsLegenda` | VARCHAR(500) | sim | não | não |
| `idDomPai` | INT | sim | não | não |
| `flgDomAtivo` | BIT | não | não | não |
| `atributos` | VARCHAR(MAX) | sim | não | não |

## Chaves estrangeiras

- `dbo.CondDadDominioAcao` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.CondDadDominio` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadDominioDefaultPat` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadDominioDefault` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadDominio` (idDomPai) → `dbo.DadDominio` (idDom)
- `dbo.DadDominio` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadValorDominioPatSolicitacao` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadValorDominioPat` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadValorDominio` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.PerfilAcessoCargo` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.RelacaoAtribuicaoDom` (idDom) → `dbo.DadDominio` (idDom)
