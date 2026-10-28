---
gerado: sincronizacao
---

# dbo.QPOQQ

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idQpoqq` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `idFrmPapel` | INT | não | não | não |
| `idFrmStatus` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.PatOpQPOQQ` (idQpoqq) → `dbo.QPOQQ` (idQpoqq)
- `dbo.QPOQQAcesso` (idQPOQQ) → `dbo.QPOQQ` (idQpoqq)
- `dbo.QPOQQ` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.QPOQQ` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.QPOQQ` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
