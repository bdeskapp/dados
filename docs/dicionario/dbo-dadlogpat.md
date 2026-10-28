---
gerado: sincronizacao
---

# dbo.DadLogPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idDadConPat` | INT | não | sim | não |
| `dtAlteracao` | DATETIME | não | sim | não |
| `numero` | DECIMAL(17,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `flgSys` | BIT | não | não | não |
| `idPatMov` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadLogDominioPat` (idPat, idDadConPat, dtAlteracao) → `dbo.DadLogPat` (idPat, idDadConPat, dtAlteracao)
- `dbo.DadLogPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadLogPat` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.DadLogPat` (idPat) → `dbo.Patrimonio` (idPat)
