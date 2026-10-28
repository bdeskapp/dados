---
gerado: sincronizacao
---

# dbo.DadCondicao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCon` | INT | não | não | não |
| `idDadAfetado` | INT | sim | não | não |
| `idDadCond` | INT | não | não | não |
| `tpCond` | CHAR(1) | não | não | não |
| `tpPreenchido` | TINYINT | sim | não | não |
| `tpBoolean` | TINYINT | sim | não | não |
| `valNumerico1` | DECIMAL(15,4) | sim | não | não |
| `valNumerico2` | DECIMAL(15,4) | sim | não | não |
| `valDominio` | VARCHAR(500) | sim | não | não |
| `tpOper` | CHAR(7) | sim | não | não |
| `dsCond` | VARCHAR(4000) | não | não | não |
| `idDadCondicao` | INT | não | sim | não |
| `iOnde` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.DadCondicao` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadCondicao` (idDadCond) → `dbo.DadoAdicional` (idDad)
- `dbo.DadCondicao` (idDadAfetado) → `dbo.DadoAdicional` (idDad)
