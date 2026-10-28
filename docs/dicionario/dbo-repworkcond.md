---
gerado: sincronizacao
---

# dbo.RepWorkCond

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `nSeq` | INT | não | sim | não |
| `idCampo` | INT | sim | não | não |
| `idDad` | INT | sim | não | não |
| `idCon` | INT | sim | não | não |
| `dsCond` | VARCHAR(3000) | sim | não | não |
| `dsCondDescription` | VARCHAR(6000) | sim | não | não |
| `dsConnect` | VARCHAR(10) | sim | não | não |
| `nOrder` | INT | sim | não | não |
| `flgFluxo` | BIT | sim | não | não |

## Chaves estrangeiras

- `dbo.RepWorkCond` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.RepWorkCond` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepWorkCond` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepWorkCond` (idPesquisa) → `dbo.RepWork` (idPesquisa)
