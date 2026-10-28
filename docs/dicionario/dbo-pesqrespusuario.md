---
gerado: sincronizacao
---

# dbo.PesqRespUsuario

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesq` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtResposta` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.PesqRespUsuario` (idPesq) → `dbo.Pesquisa` (idPesq)
- `dbo.PesqRespUsuario` (idUsu) → `dbo.Usuario` (idUsu)
