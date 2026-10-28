---
gerado: sincronizacao
---

# dbo.UnidadeMedida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUnm` | INT | não | sim | não |
| `dsUnm` | VARCHAR(10) | não | não | não |
| `flgUnmAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Atributo` (idUnm) → `dbo.UnidadeMedida` (idUnm)
- `dbo.InventarioConfig` (idUnm) → `dbo.UnidadeMedida` (idUnm)
