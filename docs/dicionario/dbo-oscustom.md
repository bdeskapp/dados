---
gerado: sincronizacao
---

# dbo.OSCustom

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOs` | INT | não | sim | não |
| `flgPrioridade` | CHAR(1) | sim | não | não |

## Chaves estrangeiras

- `dbo.OSCustom` (idOs) → `dbo.OS` (idOs)
