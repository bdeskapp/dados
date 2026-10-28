---
gerado: sincronizacao
---

# dbo.RotinaFavorita

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idFrm` | INT | não | sim | não |
| `idProc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RotinaFavorita` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.RotinaFavorita` (idUsu) → `dbo.Usuario` (idUsu)
