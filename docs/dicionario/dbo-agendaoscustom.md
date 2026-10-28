---
gerado: sincronizacao
---

# dbo.AgendaOSCustom

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAge` | INT | não | sim | não |
| `idCus` | INT | não | sim | não |
| `valor` | VARCHAR(4000) | não | não | não |

## Chaves estrangeiras

- `dbo.AgendaOSCustom` (idAge) → `dbo.AgendaOS` (IdAge)
- `dbo.AgendaOSCustom` (idCus) → `dbo.Custom` (idCus)
