---
gerado: sincronizacao
---

# dbo.LicAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.LicAlerta` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.LicAlerta` (idUsu) → `dbo.Usuario` (idUsu)
