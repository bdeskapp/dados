---
gerado: sincronizacao
---

# dbo.Minuta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMinuta` | INT | não | sim | não |
| `dsTitulo` | VARCHAR(200) | não | não | não |
| `dsMinuta` | TEXT | não | não | não |
| `idFrm` | INT | não | não | não |
| `idTar` | INT | sim | não | não |
| `idUsuCreate` | INT | não | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `idGru` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.Minuta` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Minuta` (idGru) → `dbo.GrupoAcesso` (idGru)
- `dbo.Minuta` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.Minuta` (idUsuCreate) → `dbo.Usuario` (idUsu)
- `dbo.ReqMinutaConcluida` (idMinuta) → `dbo.Minuta` (idMinuta)
- `dbo.ReqMinutaHistConcluida` (idMinuta) → `dbo.Minuta` (idMinuta)
- `dbo.ReqMinutaHistorico` (idMinuta) → `dbo.Minuta` (idMinuta)
- `dbo.ReqMinuta` (idMinuta) → `dbo.Minuta` (idMinuta)
