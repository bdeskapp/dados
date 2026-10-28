---
gerado: sincronizacao
---

# dbo.DadDomTabDefaultPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadConPat` | INT | não | não | não |
| `idDomQQ` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.DadDomTabDefaultPat` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
