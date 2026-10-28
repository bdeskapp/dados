---
gerado: sincronizacao
---

# dbo.Condicao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `tpCondicao` | CHAR(1) | não | não | não |
| `dsCondicao` | VARCHAR(100) | sim | não | não |
| `tpContexto` | CHAR(1) | não | não | não |
| `idFrm` | INT | sim | não | não |
| `idProc` | INT | sim | não | não |
| `idRotina` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CondCamposFormOrigem` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCamposImpactoNivel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCamposUrgenciaNivel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCampos` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondDad` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondPapel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondStatus` (idCond) → `dbo.Condicao` (idCond)
- `dbo.Condicao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.Condicao` (idProc) → `dbo.Processo` (idProc)
- `dbo.Condicao` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoCondicao` (idCond) → `dbo.Condicao` (idCond)
- `dbo.ReqPendConcluida` (idCond) → `dbo.Condicao` (idCond)
- `dbo.ReqPendencia` (idCond) → `dbo.Condicao` (idCond)
- `dbo.TransicaoCondicional` (idCond) → `dbo.Condicao` (idCond)
