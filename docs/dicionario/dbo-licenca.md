---
gerado: sincronizacao
---

# dbo.Licenca

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `qtdTotal` | INT | não | não | não |
| `qtdUso` | INT | não | não | não |
| `qtdAloc` | INT | não | não | não |
| `qtdDispUso` | computada | sim | não | sim |
| `tpAlerta` | CHAR(1) | não | não | não |
| `qtdMin` | SMALLINT | não | não | não |
| `idUltimaCompra` | INT | sim | não | não |
| `qtdDispAloc` | computada | sim | não | sim |

## Chaves estrangeiras

- `dbo.Licenca` (idUltimaCompra) → `dbo.LicMovimento` (idPatMov)
- `dbo.Licenca` (idPat) → `dbo.Patrimonio` (idPat)
