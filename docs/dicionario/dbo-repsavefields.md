---
gerado: sincronizacao
---

# dbo.RepSaveFields

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

- `dbo.RepSaveFields` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepSaveFields` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepSaveFields` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepSaveFields` (idPesquisa) → `dbo.RepSave` (idPesquisa)
