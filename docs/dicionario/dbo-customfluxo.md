---
gerado: sincronizacao
---

# dbo.CustomFluxo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCon` | INT | não | sim | não |
| `idFlu` | INT | não | sim | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CustomFluxo` (idCon) → `dbo.CustomConjunto` (idCon)
- `dbo.CustomFluxo` (idFlu) → `dbo.Fluxo` (idFlu)
