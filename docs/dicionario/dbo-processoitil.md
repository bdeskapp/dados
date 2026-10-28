---
gerado: sincronizacao
---

# dbo.ProcessoITIL

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdITIL` | CHAR(3) | não | sim | não |
| `dsDisciplina` | VARCHAR(20) | não | não | não |
| `dsProcITIL` | VARCHAR(40) | sim | não | não |

## Chaves estrangeiras

- `dbo.Formulario` (cdProcITIL) → `dbo.ProcessoITIL` (cdITIL)
