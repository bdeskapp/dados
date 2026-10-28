---
gerado: sincronizacao
---

# dbo.PatAlertaResumo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatAlertaRes` | INT | não | sim | não |
| `idTpp` | INT | não | não | não |
| `idUsuDest` | INT | não | não | não |
| `dsAssunto` | VARCHAR(250) | não | não | não |
| `dsNot` | TEXT | não | não | não |
| `dtGravacao` | DATETIME | não | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `dsErro` | VARCHAR(500) | sim | não | não |
| `emailErro` | VARCHAR(100) | sim | não | não |
| `dtErro` | DATETIME | sim | não | não |
| `nTentativa` | TINYINT | sim | não | não |

## Chaves estrangeiras

- `dbo.PatAlertaResumo` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.PatAlertaResumo` (idUsuDest) → `dbo.Usuario` (idUsu)
