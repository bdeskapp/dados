---
gerado: sincronizacao
---

# dbo.DadLogDominio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQQ` | INT | não | não | não |
| `idDadCon` | INT | não | não | não |
| `dtAlteracao` | DATETIME | não | não | não |
| `idDom` | INT | não | não | não |
| `nSeq` | SMALLINT | não | não | não |
| `idDadLog` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.DadLogDominio` (idDadLog) → `dbo.DadLog` (idDadLog)
