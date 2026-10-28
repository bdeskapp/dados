---
gerado: sincronizacao
---

# dbo.RegraProcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRegra` | INT | não | sim | não |
| `tpRegra` | CHAR(1) | não | não | não |
| `dsRegra` | VARCHAR(500) | não | não | não |
| `dsComando` | VARCHAR(3000) | não | não | não |
| `flgAtiva` | BIT | não | não | não |
| `dsCorrecao` | VARCHAR(3000) | sim | não | não |

## Chaves estrangeiras

- `dbo.ProcessoValida` (idRegra) → `dbo.RegraProcesso` (idRegra)
