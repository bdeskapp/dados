---
gerado: sincronizacao
---

# dbo.FormPapelEdit

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapelEdit` | INT | não | sim | não |
| `idFrmPapelStatus` | INT | não | não | não |
| `tpOperacao` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelEdit` (idFrmPapelStatus) → `dbo.FormPapelStatus` (idFrmPapelStatus)
