---
gerado: sincronizacao
---

# dbo.FormNotificacaoAlerta

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmNotAlerta` | INT | não | sim | não |
| `idFrmNotMsg` | INT | não | não | não |
| `idFrmStatus` | INT | não | não | não |
| `idFrmPapel` | INT | não | não | não |
| `nTempoAlerta` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.FormNotificacaoAlerta` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.FormNotificacaoAlerta` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormNotificacaoAlerta` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Notificacao` (idFrmNotAlerta) → `dbo.FormNotificacaoAlerta` (idFrmNotAlerta)
