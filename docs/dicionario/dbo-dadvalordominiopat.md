---
gerado: sincronizacao
---

# dbo.DadValorDominioPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadValPat` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadValorDominioPat` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadValorDominioPat` (idDadValPat) → `dbo.DadValorPat` (idDadValPat)
