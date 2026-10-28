---
gerado: sincronizacao
---

# dbo.OSAvaliacaoConcluida

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

- `dbo.OSAvaliacaoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
