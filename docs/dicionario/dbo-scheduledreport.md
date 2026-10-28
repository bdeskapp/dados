---
gerado: sincronizacao
---

# dbo.ScheduledReport

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `ScheduledReportID` | INT | não | sim | não |
| `ReportID` | INT | não | não | não |
| `IsBookReport` | BIT | não | não | não |
| `SendFrequenceType` | INT | não | não | não |
| `FormatType` | INT | não | não | não |
| `FirstExecutionDate` | DATETIME | sim | não | não |
| `LastExecutionDate` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.ScheduledReportSubscriber` (ScheduledReportID) → `dbo.ScheduledReport` (ScheduledReportID)
