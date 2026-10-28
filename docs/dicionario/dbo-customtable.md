---
gerado: sincronizacao
---

# dbo.CustomTable

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTab` | INT | não | sim | não |
| `nmTab` | VARCHAR(50) | não | não | não |
| `Cliente` | VARCHAR(5) | sim | não | não |
| `CampoFlgAtivo` | VARCHAR(255) | sim | não | não |
| `flgTpTab` | VARCHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.Custom` (idTab) → `dbo.CustomTable` (idTab)
