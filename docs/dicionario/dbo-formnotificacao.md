---
gerado: sincronizacao
---

# dbo.FormNotificacao

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmNot` | INT | não | sim | não |
| `idFrmAcao` | INT | não | não | não |
| `idFrmPapel` | INT | não | não | não |
| `idFrmNotMsg` | INT | não | não | não |
| `flgBloqueio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormNotificacao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
- `dbo.FormNotificacao` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.FormNotificacao` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.NotificacaoExt` (idFrmNot) → `dbo.FormNotificacao` (idFrmNot)
- `dbo.Notificacao` (idFrmNot) → `dbo.FormNotificacao` (idFrmNot)
