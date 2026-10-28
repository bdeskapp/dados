---
gerado: sincronizacao
---

# dbo.FormPapelRelacionado

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | não | não |
| `idTpPapel` | SMALLINT | não | não | não |
| `idFrmPapelRelacionado` | INT | não | sim | não |
| `idTpPapelRelacionado` | SMALLINT | não | não | não |
| `flgOpcional` | BIT | não | não | não |
| `flgSubGrupo` | BIT | não | não | não |
| `idListaIC` | INT | sim | não | não |
| `flgCoordenador` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelRelacionado` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelRelacionado` (idFrmPapelRelacionado) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelRelacionado` (idListaIC) → `dbo.ListaIC` (idListaIC)
- `dbo.FormPapelRelacionado` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
- `dbo.FormPapelRelacionado` (idTpPapelRelacionado) → `dbo.TipoPapel` (idTpPapel)
