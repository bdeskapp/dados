---
gerado: sincronizacao
---

# dbo.FormRequerAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmAcao` | INT | não | sim | não |
| `idFrmPapel` | INT | não | sim | não |
| `idFrmAcaoRequerida` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormRequerAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRequerAcao` (idFrmAcaoRequerida) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormRequerAcao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
