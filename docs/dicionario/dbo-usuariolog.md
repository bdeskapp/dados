---
gerado: sincronizacao
---

# dbo.UsuarioLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLog` | INT | não | sim | não |
| `idUsuResponsavelLog` | INT | não | não | não |
| `dtLog` | DATETIME | não | não | não |
| `idUsu` | INT | não | não | não |
| `nmColuna` | VARCHAR(100) | não | não | não |
| `valAnterior` | VARCHAR(1200) | sim | não | não |
| `valAtual` | VARCHAR(1200) | sim | não | não |

## Chaves estrangeiras

- `dbo.UsuarioLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.UsuarioLog` (idUsuResponsavelLog) → `dbo.Usuario` (idUsu)
