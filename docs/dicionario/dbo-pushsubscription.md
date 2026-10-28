---
gerado: sincronizacao
---

# dbo.PushSubscription

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [push e notificações](../fora-de-escopo/push.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPushSub` | INT | não | sim | não |
| `idUsu` | INT | não | não | não |
| `dsEndpoint` | VARCHAR(500) | não | não | não |
| `dsP256dh` | VARCHAR(200) | não | não | não |
| `dsAuth` | VARCHAR(100) | não | não | não |
| `dsSistema` | VARCHAR(50) | não | não | não |
| `dtCriacao` | DATETIME | não | não | não |
| `dtUltimoUso` | DATETIME | sim | não | não |
| `flgAtivo` | BIT | não | não | não |
