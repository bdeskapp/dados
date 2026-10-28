---
gerado: sincronizacao
---

# dbo.FormPesquisa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPesq` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `idProc` | INT | sim | não | não |
| `idPesq` | INT | não | não | não |
| `dtIniVigencia` | DATETIME | não | não | não |
| `dtFimVigencia` | DATETIME | sim | não | não |
| `tpCritVip` | CHAR(1) | sim | não | não |
| `tpCritPrazo` | CHAR(1) | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPesqCriterio` (idFrmPesq) → `dbo.FormPesquisa` (idFrmPesq)
- `dbo.FormPesquisa` (idPesq) → `dbo.Pesquisa` (idPesq)
