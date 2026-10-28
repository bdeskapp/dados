---
gerado: sincronizacao
---

# dbo.BubDestino

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpPapel` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |
| `idBub` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.BubDestino` (idBub) → `dbo.Bub` (idBub)
- `dbo.BubDestino` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
