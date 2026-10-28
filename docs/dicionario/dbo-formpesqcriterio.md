---
gerado: sincronizacao
---

# dbo.FormPesqCriterio

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCrit` | INT | não | sim | não |
| `idFrmPesq` | INT | não | não | não |
| `idGru` | INT | sim | não | não |
| `idCat` | INT | sim | não | não |
| `idSca` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `idTpTa` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPesqCriterio` (idFrmPesq) → `dbo.FormPesquisa` (idFrmPesq)
- `dbo.FormPesqCriterio` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
