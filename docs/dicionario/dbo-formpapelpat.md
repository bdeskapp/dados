---
gerado: sincronizacao
---

# dbo.FormPapelPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `tpBusca` | CHAR(4) | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelPat` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
