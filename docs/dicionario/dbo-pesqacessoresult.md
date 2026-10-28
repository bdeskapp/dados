---
gerado: sincronizacao
---

# dbo.PesqAcessoResult

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesq` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.PesqAcessoResult` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.PesqAcessoResult` (idPesq) → `dbo.Pesquisa` (idPesq)
