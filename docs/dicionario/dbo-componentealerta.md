---
gerado: sincronizacao
---

# dbo.ComponenteAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLoc` | INT | sim | não | não |
| `idAtr` | INT | não | não | não |
| `idUsu` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ComponenteAlerta` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteAlerta` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteAlerta` (idUsu) → `dbo.Usuario` (idUsu)
