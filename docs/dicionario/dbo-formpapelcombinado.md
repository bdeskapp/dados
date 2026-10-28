---
gerado: sincronizacao
---

# dbo.FormPapelCombinado

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | não | não |
| `idFrmPapelCombinado` | INT | não | sim | não |
| `flgOpcional` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelCombinado` (idFrmPapelCombinado) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelCombinado` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
