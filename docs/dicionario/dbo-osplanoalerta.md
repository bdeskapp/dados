---
gerado: sincronizacao
---

# dbo.OSPlanoAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOS` | INT | não | sim | não |
| `Percentual` | INT | não | sim | não |
| `DataEnvio` | DATETIME | não | não | não |
| `FlgEnvioOk` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.OSPlanoAlerta` (idOS) → `dbo.OS` (idOs)
