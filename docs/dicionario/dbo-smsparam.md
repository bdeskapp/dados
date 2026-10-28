---
gerado: sincronizacao
---

# dbo.SMSParam

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Url` | VARCHAR(MAX) | não | não | não |
| `cdOrigem` | CHAR(100) | não | não | não |
| `nMaxChar` | SMALLINT | não | não | não |
| `cdErroTransitorio` | VARCHAR(MAX) | não | não | não |
| `nTentativa` | TINYINT | não | não | não |
| `nIntervalo` | TINYINT | não | não | não |
| `cdErroPermanente` | VARCHAR(MAX) | sim | não | não |
| `emailErro` | VARCHAR(MAX) | não | não | não |
| `nRetencao` | TINYINT | não | não | não |
