---
gerado: sincronizacao
---

# dbo.CondDadDominioAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idDadCon` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CondDadDominioAcao` (idCond) → `dbo.CondicaoAcao` (idCond)
- `dbo.CondDadDominioAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.CondDadDominioAcao` (idDom) → `dbo.DadDominio` (idDom)
