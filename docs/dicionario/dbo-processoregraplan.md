---
gerado: sincronizacao
---

# dbo.ProcessoRegraPlan

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idProc` | INT | não | não | não |
| `idRotina` | INT | não | sim | não |
| `idRotinaPlan` | INT | não | sim | não |
| `flgIni` | BIT | não | não | não |
| `flgFim` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ProcessoRegraPlan` (idProc) → `dbo.Processo` (idProc)
- `dbo.ProcessoRegraPlan` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.ProcessoRegraPlan` (idRotinaPlan) → `dbo.Rotina` (idRotina)
