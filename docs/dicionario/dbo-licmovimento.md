---
gerado: sincronizacao
---

# dbo.LicMovimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatMov` | INT | não | sim | não |
| `qtdLic` | INT | não | não | não |
| `valUnit` | MONEY | não | não | não |
| `dsFornecedor` | VARCHAR(100) | sim | não | não |
| `dsNF` | VARCHAR(10) | sim | não | não |
| `dtRenov` | DATETIME | sim | não | não |
| `idReqAge` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.LicMovimento` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.Licenca` (idUltimaCompra) → `dbo.LicMovimento` (idPatMov)
