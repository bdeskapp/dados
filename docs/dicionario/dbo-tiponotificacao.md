---
gerado: sincronizacao
---

# dbo.TipoNotificacao

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpNot` | INT | não | sim | não |
| `dsTpNot` | VARCHAR(30) | não | não | não |
| `objNot` | VARCHAR(50) | não | não | não |
| `colBusca` | VARCHAR(100) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormNotMensagem` (idTpNot) → `dbo.TipoNotificacao` (idTpNot)
