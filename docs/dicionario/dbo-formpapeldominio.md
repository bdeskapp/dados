---
gerado: sincronizacao
---

# dbo.FormPapelDominio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `idTpPapel` | SMALLINT | não | sim | não |
| `idTpPapelDom` | SMALLINT | não | sim | não |
| `idPart` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormPapelDominio` (idFrmPapel, idTpPapel) → `dbo.FormPapelTipo` (idFrmPapel, idTpPapel)
- `dbo.FormPapelDominio` (idTpPapelDom, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
