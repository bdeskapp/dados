---
gerado: sincronizacao
---

# dbo.SyncEmailLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `IdSyncEmailLog` | INT | não | não | não |
| `IdSyncEmail` | INT | não | não | não |
| `dsLog` | TEXT | não | não | não |
| `dsAcao` | VARCHAR(10) | não | não | não |
| `dsAgente` | VARCHAR(150) | sim | não | não |
| `dtLog` | DATETIME | não | não | não |
