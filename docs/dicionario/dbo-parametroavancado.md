---
gerado: sincronizacao
---

# dbo.ParametroAvancado

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPar` | INT | não | sim | não |
| `chavePar` | VARCHAR(150) | não | não | não |
| `descricao` | VARCHAR(500) | não | não | não |
| `valorPar` | VARCHAR(MAX) | não | não | não |
| `dadosPreProcessamento` | VARCHAR(MAX) | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ParametroAvancado` (idUsuOperacao) → `dbo.Usuario` (idUsu)
