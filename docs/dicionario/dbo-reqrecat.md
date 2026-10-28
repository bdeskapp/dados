---
gerado: sincronizacao
---

# dbo.ReqRecat

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqRecat` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idReqHist` | INT | não | não | não |
| `dtRecat` | DATETIME | não | não | não |
| `idUsu` | INT | não | não | não |
| `idGruAnt` | INT | não | não | não |
| `idGruAtual` | INT | não | não | não |
| `idTarAnt` | INT | não | não | não |
| `idTarAtual` | INT | não | não | não |
| `slaAnt` | REAL | não | não | não |
| `slaAtual` | REAL | não | não | não |
| `dtFimPrevAnt` | DATETIME | não | não | não |
| `dtFimPrevAtual` | DATETIME | não | não | não |
| `idMotivo` | INT | sim | não | não |
| `flgKB_P_Ant` | BIT | não | não | não |
| `flgKB_S_Ant` | BIT | não | não | não |
| `flgKB_P_Atual` | BIT | não | não | não |
| `flgKB_S_Atual` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqRecat` (idMotivo) → `dbo.FormAcaoMotivo` (idMotivo)
- `dbo.ReqRecat` (idGruAnt) → `dbo.Grupo` (idGru)
- `dbo.ReqRecat` (idGruAtual) → `dbo.Grupo` (idGru)
- `dbo.ReqRecat` (idTarAnt) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecat` (idTarAtual) → `dbo.Tarefa` (idTar)
- `dbo.ReqRecat` (idUsu) → `dbo.Usuario` (idUsu)
