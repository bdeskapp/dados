---
gerado: sincronizacao
---

# dbo.FormPapelTipo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormPapelDominio` (idFrmPapel, idTpPapel) → `dbo.FormPapelTipo` (idFrmPapel, idTpPapel)
- `dbo.FormPapelTipo` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelTipo` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
