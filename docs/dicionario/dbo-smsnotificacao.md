---
gerado: sincronizacao
---

# dbo.SMSNotificacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSMSNot` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqHist` | INT | não | não | não |
| `dsMsg` | VARCHAR(MAX) | não | não | não |
| `dtRegistro` | DATETIME | não | não | não |
| `flgEnvio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.SMSNotificacaoUsu` (idSMSNot) → `dbo.SMSNotificacao` (idSMSNot)
