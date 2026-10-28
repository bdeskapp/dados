---
gerado: sincronizacao
---

# dbo.ProcHistAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | não | não |
| `idRotina` | INT | não | não | não |
| `idRotinaAcesso` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ProcHistAcesso` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.ProcHistAcesso` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ProcHistAcesso` (idRotinaAcesso) → `dbo.Rotina` (idRotina)
