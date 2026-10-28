---
gerado: sincronizacao
---

# dbo.DadFormPapelStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idFrmPapelStatus` | INT | não | sim | não |
| `flgVisivel` | BIT | não | não | não |
| `flgModificar` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadFormPapelStatus` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadFormPapelStatus` (idFrmPapelStatus) → `dbo.FormPapelStatus` (idFrmPapelStatus)
