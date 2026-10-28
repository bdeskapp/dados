---
gerado: sincronizacao
---

# dbo.DadValorDominioPatSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadValPatSol` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadValorDominioPatSolicitacao` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadValorDominioPatSolicitacao` (idDadValPatSol) → `dbo.DadValorPatSolicitacao` (idDadValPatSol)
