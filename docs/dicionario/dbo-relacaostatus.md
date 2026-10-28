---
gerado: sincronizacao
---

# dbo.RelacaoStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelStatus` | INT | não | sim | não |
| `idRel` | INT | não | não | não |
| `idRotina` | INT | não | não | não |
| `idFrmStatus` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RelacaoStatus` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoStatus` (idRel) → `dbo.Relacao` (idRel)
- `dbo.RelacaoStatus` (idRotina) → `dbo.Rotina` (idRotina)
