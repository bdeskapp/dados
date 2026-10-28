---
gerado: sincronizacao
---

# dbo.GrupoAcessoFluxo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idFlu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.GrupoAcessoFluxo` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.GrupoAcessoFluxo` (idGru) → `dbo.GrupoAcesso` (idGru)
