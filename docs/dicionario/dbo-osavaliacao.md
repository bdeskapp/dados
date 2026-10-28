---
gerado: sincronizacao
---

# dbo.OSAvaliacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOS` | INT | não | sim | não |
| `dtIniOSAval` | DATETIME | não | não | não |
| `dtFimOSAval` | DATETIME | sim | não | não |
| `tpAval` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.OSAvaliacao` (idOS) → `dbo.OS` (idOs)
