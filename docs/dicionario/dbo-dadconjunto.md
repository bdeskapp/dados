---
gerado: sincronizacao
---

# dbo.DadConjunto

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCon` | INT | não | sim | não |
| `dsCon` | VARCHAR(50) | não | não | não |
| `observacao` | VARCHAR(250) | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgConAtivo` | BIT | não | não | não |
| `flgMultiplo` | BIT | não | não | não |
| `flgPermitirUpload` | BIT | não | não | não |
| `flgTabela` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadColecao` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadCondicao` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadContextoCampo` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadContextoPat` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.InventarioConfigDA` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepSaveCond` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepSaveFields` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepWorkCond` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepWorkFields` (idCon) → `dbo.DadConjunto` (idCon)
