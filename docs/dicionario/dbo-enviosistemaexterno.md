---
gerado: sincronizacao
---

# dbo.EnvioSistemaExterno

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `id` | INT | não | sim | não |
| `idEvento` | INT | não | não | não |
| `status` | VARCHAR(20) | sim | não | não |
| `sistema` | VARCHAR(100) | sim | não | não |
| `conteudo` | VARCHAR(MAX) | sim | não | não |
| `dtUltimaTentativaEnvio` | DATETIME | sim | não | não |
| `nTentativas` | SMALLINT | sim | não | não |
| `logEnvio` | VARCHAR(MAX) | sim | não | não |

## Chaves estrangeiras

- `dbo.EnvioSistemaExterno` (idEvento) → `dbo.RequisicaoEvento` (idEvento)
