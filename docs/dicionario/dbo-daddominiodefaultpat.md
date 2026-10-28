---
gerado: sincronizacao
---

# dbo.DadDominioDefaultPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadConPat` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadDominioDefaultPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadDominioDefaultPat` (idDom) → `dbo.DadDominio` (idDom)
