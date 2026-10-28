---
gerado: sincronizacao
---

# dbo.RelacaoAtribuicaoTab

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idDomQQ` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RelacaoAtribuicaoTab` (idRelEfeito) → `dbo.RelacaoAtribuicao` (idRelEfeito)
