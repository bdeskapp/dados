---
gerado: sincronizacao
---

# dbo.CondCampos

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `dsColuna` | VARCHAR(50) | não | não | não |
| `tpColuna` | CHAR(1) | não | não | não |
| `tpOperador` | CHAR(6) | não | não | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |

## Chaves estrangeiras

- `dbo.CondCampos` (idCond) → `dbo.Condicao` (idCond)
