---
gerado: sincronizacao
---

# dbo.ObjectQueryParam

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idParam` | INT | não | sim | não |
| `cdObj` | INT | não | não | não |
| `nSeq` | TINYINT | não | não | não |
| `nmParam` | NVARCHAR(50) | não | não | não |
| `dsLabel` | NVARCHAR(MAX) | não | não | não |
| `tpParam` | CHAR(1) | não | não | não |
| `cmdQuery` | NVARCHAR(MAX) | sim | não | não |
| `flgRequired` | BIT | não | não | não |
| `idParent` | INT | sim | não | não |
| `flgRequiredParent` | BIT | sim | não | não |
| `relatedNmParam` | NVARCHAR(50) | sim | não | não |
| `tpRule` | CHAR(1) | sim | não | não |
| `dsTermoValidateMessage` | NVARCHAR(1000) | sim | não | não |
| `flgAutoInSummary` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ObjectQueryParam` (cdObj) → `dbo.ObjectQuery` (cdObj)
- `dbo.ObjectQueryParam` (idParent) → `dbo.ObjectQueryParam` (idParam)
