---
gerado: sincronizacao
---

# dbo.DadValorPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadValPat` | INT | não | sim | não |
| `idPat` | INT | não | não | não |
| `idDadConPat` | INT | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `numero` | DECIMAL(17,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadValorDominioPat` (idDadValPat) → `dbo.DadValorPat` (idDadValPat)
- `dbo.DadValorPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadValorPat` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.DadValorTabelaPat` (idDadValPat) → `dbo.DadValorPat` (idDadValPat)
