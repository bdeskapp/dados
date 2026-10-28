---
gerado: sincronizacao
---

# dbo.RepEntidade

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEntidade` | INT | não | sim | não |
| `Descricao` | CHAR(50) | não | não | não |
| `idTabCus` | INT | não | não | não |
| `dsChave` | CHAR(25) | não | não | não |
| `dsObs` | VARCHAR(250) | sim | não | não |
| `dsObsCampos` | VARCHAR(250) | sim | não | não |

## Chaves estrangeiras

- `dbo.RepDetCampos` (idEntidade) → `dbo.RepEntidade` (idEntidade)
- `dbo.RepSave` (idEntidade) → `dbo.RepEntidade` (idEntidade)
- `dbo.RepWork` (idEntidade) → `dbo.RepEntidade` (idEntidade)
