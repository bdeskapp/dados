---
gerado: sincronizacao
---

# dbo.CategoriaFluxo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCatFlu` | INT | não | sim | não |
| `dsCatFlu` | VARCHAR(30) | não | não | não |
| `flgCatFluAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Fluxo` (idCatFlu) → `dbo.CategoriaFluxo` (idCatFlu)
