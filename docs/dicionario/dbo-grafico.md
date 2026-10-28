---
gerado: sincronizacao
---

# dbo.Grafico

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdGrafico` | CHAR(10) | não | sim | não |
| `dsGrafico` | VARCHAR(30) | não | não | não |
| `flgMulti` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ObjectQuery` (cdChart) → `dbo.Grafico` (cdGrafico)
- `dbo.RelCust` (cdGrafico) → `dbo.Grafico` (cdGrafico)
