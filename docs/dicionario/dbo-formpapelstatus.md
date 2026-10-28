---
gerado: sincronizacao
---

# dbo.FormPapelStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapelStatus` | INT | não | sim | não |
| `idFrmPapel` | INT | não | não | não |
| `idFrmStatus` | INT | sim | não | não |
| `flgVisivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadFormPapelStatus` (idFrmPapelStatus) → `dbo.FormPapelStatus` (idFrmPapelStatus)
- `dbo.FormPapelEdit` (idFrmPapelStatus) → `dbo.FormPapelStatus` (idFrmPapelStatus)
- `dbo.FormPapelStatus` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
