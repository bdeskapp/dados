---
gerado: sincronizacao
---

# dbo.ScheduledReportSubscriber

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `ScheduledReportID` | INT | não | não | não |
| `SubscriberID` | INT | não | não | não |
| `Email` | VARCHAR(200) | não | não | não |

## Chaves estrangeiras

- `dbo.ScheduledReportSubscriber` (ScheduledReportID) → `dbo.ScheduledReport` (ScheduledReportID)
- `dbo.ScheduledReportSubscriber` (SubscriberID) → `dbo.Usuario` (idUsu)
