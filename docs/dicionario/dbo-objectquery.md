---
gerado: sincronizacao
---

# dbo.ObjectQuery

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdObj` | INT | não | sim | não |
| `cmdQuery` | NVARCHAR(MAX) | não | não | não |
| `cmdQueryTotal` | NVARCHAR(MAX) | sim | não | não |
| `cmdQueryChart` | NVARCHAR(MAX) | sim | não | não |
| `xslOutput` | NVARCHAR(50) | sim | não | não |
| `flgGrid` | BIT | não | não | não |
| `flgChart` | BIT | não | não | não |
| `cdChart` | CHAR(10) | sim | não | não |
| `xmlChartParam` | NVARCHAR(300) | sim | não | não |

## Chaves estrangeiras

- `dbo.ObjectQueryParam` (cdObj) → `dbo.ObjectQuery` (cdObj)
- `dbo.ObjectQuery` (cdChart) → `dbo.Grafico` (cdGrafico)
- `dbo.ObjectQuery` (cdObj) → `dbo.Object` (cdObj)
- `dbo.ObjectSummaryDetail` (cdObjQuery) → `dbo.ObjectQuery` (cdObj)
