---
gerado: sincronizacao
---

# dbo.RelacaoAtribuicaoDom

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RelacaoAtribuicaoDom` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.RelacaoAtribuicaoDom` (idRelEfeito) → `dbo.RelacaoAtribuicao` (idRelEfeito)
