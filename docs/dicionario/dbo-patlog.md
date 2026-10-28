---
gerado: sincronizacao
---

# dbo.PatLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLog` | INT | não | sim | não |
| `dtLog` | DATETIME | não | não | não |
| `idUsu` | INT | sim | não | não |
| `idPat` | INT | não | não | não |
| `idPatMov` | INT | sim | não | não |
| `dsColuna` | VARCHAR(50) | não | não | não |
| `valAnterior` | VARCHAR(250) | sim | não | não |
| `valAtual` | VARCHAR(250) | sim | não | não |

## Chaves estrangeiras

- `dbo.PatLog` (idPatMov) → `dbo.PatMovimento` (idPatMov)
- `dbo.PatLog` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatLog` (idUsu) → `dbo.Usuario` (idUsu)
