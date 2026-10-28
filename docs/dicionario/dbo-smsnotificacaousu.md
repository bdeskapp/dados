---
gerado: sincronizacao
---

# dbo.SMSNotificacaoUsu

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSMSNot` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `nuProtocolo` | VARCHAR(MAX) | sim | não | não |
| `cdStatus` | VARCHAR(MAX) | sim | não | não |
| `cdStatusCarrier` | VARCHAR(MAX) | sim | não | não |
| `cdStatusMobile` | VARCHAR(MAX) | sim | não | não |
| `dtConsulta` | DATETIME | sim | não | não |
| `nTentativas` | TINYINT | sim | não | não |
| `celular` | VARCHAR(15) | sim | não | não |

## Chaves estrangeiras

- `dbo.SMSNotificacaoUsu` (idSMSNot) → `dbo.SMSNotificacao` (idSMSNot)
- `dbo.SMSNotificacaoUsu` (idUsu) → `dbo.Usuario` (idUsu)
