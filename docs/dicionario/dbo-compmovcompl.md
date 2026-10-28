---
gerado: sincronizacao
---

# dbo.CompMovCompl

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCompMov` | INT | não | sim | não |
| `dsFornecedor` | VARCHAR(50) | sim | não | não |
| `dsNFiscal` | VARCHAR(10) | sim | não | não |
| `valUnitario` | MONEY | sim | não | não |

## Chaves estrangeiras

- `dbo.CompMovCompl` (idCompMov) → `dbo.CompMovimento` (idCompMov)
