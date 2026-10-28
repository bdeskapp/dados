---
gerado: sincronizacao
---

# dbo.TipoPapelDominio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpPapel` | SMALLINT | não | sim | não |
| `idTpPapelDom` | SMALLINT | não | sim | não |

## Chaves estrangeiras

- `dbo.TipoPapelDominio` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.TipoPapelDominio` (idTpPapelDom) → `dbo.TipoPapel` (idTpPapel)
