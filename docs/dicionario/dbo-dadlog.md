---
gerado: sincronizacao
---

# dbo.DadLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQQ` | INT | não | não | não |
| `idDadCon` | INT | não | não | não |
| `dtAlteracao` | DATETIME | não | não | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `flgSys` | BIT | não | não | não |
| `nSeq` | SMALLINT | não | não | não |
| `idDadLog` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadLogDominio` (idDadLog) → `dbo.DadLog` (idDadLog)
- `dbo.DadLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RequisicaoEvento` (idDadLog) → `dbo.DadLog` (idDadLog)
