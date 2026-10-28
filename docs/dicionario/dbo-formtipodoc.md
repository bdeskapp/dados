---
gerado: sincronizacao
---

# dbo.FormTipoDoc

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmTpDoc` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `dsTpDoc` | VARCHAR(30) | não | não | não |
| `obsTpDoc` | VARCHAR(255) | sim | não | não |
| `tpTTL` | CHAR(1) | não | não | não |
| `nTTL` | SMALLINT | sim | não | não |
| `flgExclusaoFisica` | BIT | não | não | não |
| `nTamMax` | TINYINT | sim | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormTipoDoc` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.ProcTipoDoc` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.ReqDocConcluida` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.ReqDocumento` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailActionUpdate` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailConfig` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailNewReq` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailUpdateReq` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
