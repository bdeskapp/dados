---
gerado: sincronizacao
---

# dbo.TipoPatrimonioMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpPatMov` | INT | não | sim | não |
| `dsTpPatMov` | CHAR(50) | sim | não | não |
| `flgTpPatMovAtivo` | INT | sim | não | não |
| `flgSomenteOS` | INT | sim | não | não |
| `flgPatComp` | CHAR(1) | sim | não | não |
| `flgTpPatMov` | CHAR(1) | sim | não | não |
| `flgMovtoUnico` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.ComponenteMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
- `dbo.LicencaMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
- `dbo.PatrimonioMovimento` (idTpPatMov) → `dbo.TipoPatrimonioMovimento` (idTpPatMov)
