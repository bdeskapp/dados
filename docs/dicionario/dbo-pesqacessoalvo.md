---
gerado: sincronizacao
---

# dbo.PesqAcessoAlvo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesq` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.PesqAcessoAlvo` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.PesqAcessoAlvo` (idPesq) → `dbo.Pesquisa` (idPesq)
