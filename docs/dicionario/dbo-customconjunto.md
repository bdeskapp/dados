---
gerado: sincronizacao
---

# dbo.CustomConjunto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCon` | INT | não | sim | não |
| `idTab` | INT | não | não | não |
| `nmCon` | VARCHAR(100) | não | não | não |

## Chaves estrangeiras

- `dbo.CustomFluxo` (idCon) → `dbo.CustomConjunto` (idCon)
- `dbo.CustomTarefa` (idCon) → `dbo.CustomConjunto` (idCon)
- `dbo.Custom` (idCon) → `dbo.CustomConjunto` (idCon)
