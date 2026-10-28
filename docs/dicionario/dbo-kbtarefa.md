---
gerado: sincronizacao
---

# dbo.KBTarefa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idKB` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.KBTarefa` (idKB) → `dbo.KBase` (idKB)
- `dbo.KBTarefa` (idTar) → `dbo.Tarefa` (idTar)
