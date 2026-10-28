---
gerado: sincronizacao
---

# dbo.Justificativa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idJus` | INT | não | sim | não |
| `idGru` | INT | não | não | não |
| `dsJus` | VARCHAR(100) | não | não | não |
| `flgJusAtivo` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.Justificativa` (idGru) → `dbo.Grupo` (idGru)
- `dbo.Justificativa` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.OSHistorico` (idJus) → `dbo.Justificativa` (idJus)
- `dbo.OSHistorico` (idJusOSH) → `dbo.Justificativa` (idJus)
- `dbo.ReqHistConcluida` (idJus) → `dbo.Justificativa` (idJus)
- `dbo.ReqHistorico` (idJus) → `dbo.Justificativa` (idJus)
