---
gerado: sincronizacao
---

# dbo.FluxoOsAnexoGrupo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAne` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FluxoOsAnexoGrupo` (idAne) → `dbo.FluxoOsAnexo` (idAne)
- `dbo.FluxoOsAnexoGrupo` (idGru) → `dbo.Grupo` (idGru)
