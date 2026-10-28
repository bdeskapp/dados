---
gerado: sincronizacao
---

# dbo.PapelTipoPapel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPapel` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.PapelTipoPapel` (idPapel) → `dbo.Papel` (idPapel)
- `dbo.PapelTipoPapel` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
