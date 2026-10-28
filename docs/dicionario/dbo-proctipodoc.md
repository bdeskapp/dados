---
gerado: sincronizacao
---

# dbo.ProcTipoDoc

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotina` | INT | não | sim | não |
| `idFrmTpDoc` | INT | não | sim | não |
| `tpAcesso1` | CHAR(1) | não | não | não |
| `tpAcesso2` | CHAR(1) | não | não | não |
| `tpAcesso3` | CHAR(1) | não | não | não |
| `tpAcesso4` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.ProcTipoDoc` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.ProcTipoDoc` (idRotina) → `dbo.Rotina` (idRotina)
