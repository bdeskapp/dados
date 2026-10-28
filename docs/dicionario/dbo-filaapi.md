---
gerado: sincronizacao
---

# dbo.FilaAPI

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFilaAPI` | INT | não | sim | não |
| `corpo` | VARCHAR(MAX) | sim | não | não |
| `retorno` | VARCHAR(MAX) | sim | não | não |
| `retornoLogAmigavel` | VARCHAR(MAX) | sim | não | não |
| `retornoMensagensErro` | VARCHAR(MAX) | sim | não | não |
| `criadoPor` | VARCHAR(100) | sim | não | não |
| `processadoPor` | VARCHAR(100) | sim | não | não |
| `dtCriacao` | DATETIME | sim | não | não |
| `dtProcessamento` | DATETIME | sim | não | não |
