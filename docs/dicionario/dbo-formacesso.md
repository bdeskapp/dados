---
gerado: sincronizacao
---

# dbo.FormAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `idGru` | INT | não | sim | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgOffline` | BIT | não | não | não |
| `flgAgenda` | BIT | não | não | não |
| `flgVerbaObrigatoria` | BIT | não | não | não |
| `flgLocObrigatoria` | BIT | não | não | não |
| `flgLocEditavel` | BIT | não | não | não |
| `flgDescObrigatoria` | BIT | não | não | não |
| `flgAssuntoTarefa` | BIT | não | não | não |
| `flgMultipla` | BIT | não | não | não |
| `flgPermiteMultPapeis` | BIT | não | não | não |
| `flgCombinaREG` | BIT | não | não | não |
| `nSeq` | CHAR(10) | não | não | não |
| `flgImpUrg` | BIT | não | não | não |
| `formXML` | XML | sim | não | não |
| `xslOutput` | NVARCHAR(50) | sim | não | não |
| `flgSubGrupoPapelTipoClienteRelacREG` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormAcesso` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormAcesso` (idGru) → `dbo.GrupoAcesso` (idGru)
