---
gerado: sincronizacao
---

# dbo.Origem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOri` | INT | não | sim | não |
| `dsOrigem` | VARCHAR(255) | sim | não | não |
| `nmBanco` | VARCHAR(50) | sim | não | não |
| `flgAtiva` | BIT | não | não | não |
| `flgLinkedServer` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.OSVinculo` (idOri) → `dbo.Origem` (idOri)
