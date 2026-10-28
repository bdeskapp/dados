---
gerado: sincronizacao
---

# dbo.RepAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | não | não |
| `idAre` | INT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.RepAcesso` (idAre) → `dbo.Area` (idAre)
- `dbo.RepAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.RepAcesso` (idUsuOperacao) → `dbo.Usuario` (idUsu)
