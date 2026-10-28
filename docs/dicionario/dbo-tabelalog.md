---
gerado: sincronizacao
---

# dbo.TabelaLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLog` | INT | não | sim | não |
| `idTab` | INT | não | não | não |
| `tpOp` | CHAR(1) | não | não | não |
| `idChave` | INT | não | não | não |
| `nmCol` | VARCHAR(50) | sim | não | não |
| `valAnterior` | VARCHAR(100) | sim | não | não |
| `valAtual` | VARCHAR(100) | sim | não | não |
| `idUsu` | INT | não | não | não |
| `dtLog` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.TabelaLog` (idTab) → `dbo.Tabela` (idTab)
- `dbo.TabelaLog` (idUsu) → `dbo.Usuario` (idUsu)
