---
gerado: sincronizacao
---

# dbo.Causa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCausa` | INT | não | sim | não |
| `idFlu` | INT | não | não | não |
| `idRel` | INT | não | não | não |
| `idReqCausa` | INT | não | não | não |
| `tpCausa` | CHAR(1) | não | não | não |
| `idFrmAcaoDireta` | INT | sim | não | não |
| `idFrmStatusTO` | INT | sim | não | não |
| `flgCondEval` | BIT | sim | não | não |
| `dtReg` | DATETIME | não | não | não |
| `dtOcorr` | DATETIME | sim | não | não |
| `status` | CHAR(1) | não | não | não |
| `nSeq` | SMALLINT | não | não | não |
| `flgRepeat` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Causa` (idFrmAcaoDireta) → `dbo.FormAcao` (idFrmAcao)
- `dbo.Causa` (idFrmStatusTO) → `dbo.FormStatus` (idFrmStatus)
- `dbo.Causa` (idRel) → `dbo.Relacao` (idRel)
- `dbo.Causa` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.Efeito` (idCausa) → `dbo.Causa` (idCausa)
- `dbo.ReqTimeout` (idCausa) → `dbo.Causa` (idCausa)
