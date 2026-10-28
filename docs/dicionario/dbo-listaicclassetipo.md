---
gerado: sincronizacao
---

# dbo.ListaICClasseTipo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idListaICClassTipo` | INT | não | sim | não |
| `idListaIC` | INT | não | não | não |
| `idClas` | INT | sim | não | não |
| `idTpp` | INT | sim | não | não |
| `idUsuIni` | INT | não | não | não |
| `dtIni` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `idUsuFim` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ListaICClasseTipo` (idClas) → `dbo.Classe` (idClas)
- `dbo.ListaICClasseTipo` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.ListaICClasseTipo` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.ListaICClasseTipo` (idUsuIni) → `dbo.Usuario` (idUsu)
- `dbo.ListaICClasseTipo` (idUsuFim) → `dbo.Usuario` (idUsu)
