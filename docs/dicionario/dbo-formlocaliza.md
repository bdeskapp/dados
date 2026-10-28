---
gerado: sincronizacao
---

# dbo.FormLocaliza

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `nSeq` | SMALLINT | não | sim | não |
| `idFrm` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.FormLocaliza` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormLocaliza` (idFrm) → `dbo.Formulario` (idFrm)
