---
gerado: sincronizacao
---

# dbo.CompAlertaNotifica

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCompMin` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CompAlertaNotifica` (idCompMin) → `dbo.CompAlertaMinimo` (idCompMin)
- `dbo.CompAlertaNotifica` (idUsu) → `dbo.Usuario` (idUsu)
