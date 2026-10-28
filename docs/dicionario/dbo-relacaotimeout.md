---
gerado: sincronizacao
---

# dbo.RelacaoTimeout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRel` | INT | não | sim | não |
| `idFrmStatus` | INT | sim | não | não |
| `tpTimeOut` | CHAR(1) | não | não | não |
| `prcTimeout` | SMALLINT | sim | não | não |
| `valTimeout` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.RelacaoTimeout` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoTimeout` (idRel) → `dbo.Relacao` (idRel)
