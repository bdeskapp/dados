---
gerado: sincronizacao
---

# dbo.MarcaTipoPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMar` | INT | não | sim | não |
| `idTpp` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.MarcaTipoPat` (idMar) → `dbo.Marca` (idMar)
- `dbo.MarcaTipoPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
