---
gerado: sincronizacao
---

# dbo.VIP

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAre` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtIni` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.VIP` (idAre) → `dbo.Area` (idAre)
- `dbo.VIP` (idUsu) → `dbo.Usuario` (idUsu)
