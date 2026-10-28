---
gerado: sincronizacao
---

# dbo.TipoOSVinculo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `IdTpVnc` | INT | não | sim | não |
| `DsTpVinculo` | VARCHAR(50) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.OSVinculo` (idTpVnc) → `dbo.TipoOSVinculo` (IdTpVnc)
