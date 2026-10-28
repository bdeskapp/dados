---
gerado: sincronizacao
---

# dbo.Bub

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idBub` | INT | não | sim | não |
| `dsBub` | VARCHAR(1000) | sim | não | não |
| `tpFormato` | CHAR(1) | não | não | não |
| `nIntervalo` | TINYINT | sim | não | não |
| `dtIniBub` | DATETIME | não | não | não |
| `dtFimBub` | DATETIME | não | não | não |
| `idGru` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `nPrioridade` | INT | não | não | não |
| `flgAll` | BIT | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.BubDestino` (idBub) → `dbo.Bub` (idBub)
- `dbo.Bub` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
