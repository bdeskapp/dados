---
gerado: sincronizacao
---

# dbo.DadDominioDefault

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadDominioDefault` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadDominioDefault` (idDom) → `dbo.DadDominio` (idDom)
