---
gerado: sincronizacao
---

# dbo.DadContextoPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadConPat` | INT | não | sim | não |
| `idDad` | INT | não | não | não |
| `idCon` | INT | sim | não | não |
| `idClas` | INT | sim | não | não |
| `idTpp` | INT | sim | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `flgContextoAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoPat` (idClas) → `dbo.Classe` (idClas)
- `dbo.DadContextoPat` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadContextoPat` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadContextoPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.DadDefaultPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadDomTabDefaultPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadDominioDefaultPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadLogPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadValorPatSolicitacao` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadValorPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
