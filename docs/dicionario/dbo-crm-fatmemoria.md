---
gerado: sincronizacao
---

# dbo.CRM_FatMemoria

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFat` | INT | não | sim | não |
| `valHTBase` | MONEY | não | sim | não |
| `valHE` | MONEY | não | não | não |
| `qtdHT` | INT | não | não | não |
| `qtdHE` | INT | não | não | não |
| `qtdHTSab` | INT | não | não | não |
| `qtdHTDom` | INT | não | não | não |
| `qtdHTNot` | INT | não | não | não |
| `valTotHT` | MONEY | não | não | não |
| `valTotHE` | MONEY | não | não | não |
| `valTotSab` | MONEY | não | não | não |
| `valTotDom` | MONEY | não | não | não |
| `valTotNot` | MONEY | não | não | não |
| `nuPrcHE` | DECIMAL(5,2) | sim | não | não |
| `nuPrcSab` | DECIMAL(5,2) | sim | não | não |
| `nuPrcDom` | DECIMAL(5,2) | sim | não | não |
| `nuPrcNoturno` | DECIMAL(5,2) | sim | não | não |
| `nuHTMin` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_FatMemoria` (idFat) → `dbo.CRM_Faturamento` (idFat)
