---
gerado: sincronizacao
---

# dbo.FormNotMensagem

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmNotMsg` | INT | não | sim | não |
| `dsTitulo` | VARCHAR(100) | não | não | não |
| `dsNot` | VARCHAR(3000) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idTpNot` | INT | não | não | não |
| `idGruAdm` | INT | não | não | não |
| `cdNot` | VARCHAR(20) | não | não | não |

## Chaves estrangeiras

- `dbo.FormNotLista` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.FormNotMensagem` (idTpNot) → `dbo.TipoNotificacao` (idTpNot)
- `dbo.FormNotificacaoAlerta` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.FormNotificacao` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.RelacaoAlerta` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
