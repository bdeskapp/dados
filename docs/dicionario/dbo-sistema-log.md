---
gerado: sincronizacao
---

# dbo.Sistema_Log

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLog` | INT | não | sim | não |
| `dtLog` | DATETIME | não | não | não |
| `operacao` | VARCHAR(10) | não | não | não |
| `usuarioLog` | INT | não | não | não |
| `tabela` | VARCHAR(100) | não | não | não |
| `chavePrimaria` | INT | não | não | não |
| `chaveSecundaria` | INT | sim | não | não |
| `chaveTerciaria` | INT | sim | não | não |
| `colunaAlterada` | VARCHAR(100) | sim | não | não |
| `valorAntigo` | VARCHAR(MAX) | sim | não | não |
| `valorNovo` | VARCHAR(MAX) | sim | não | não |

## Chaves estrangeiras

- `dbo.Sistema_Log` (usuarioLog) → `dbo.Usuario` (idUsu)
