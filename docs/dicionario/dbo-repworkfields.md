---
gerado: sincronizacao
---

# dbo.RepWorkFields

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `idCampo` | INT | sim | não | não |
| `nSeq` | INT | não | sim | não |
| `idDad` | INT | sim | não | não |
| `idCon` | INT | sim | não | não |
| `flgFluxo` | BIT | sim | não | não |
| `nOrdemRel` | INT | sim | não | não |
| `idCount` | INT | sim | não | não |
| `idSum` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RepWorkFields` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepWorkFields` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepWorkFields` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepWorkFields` (idPesquisa) → `dbo.RepWork` (idPesquisa)
