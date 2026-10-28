---
gerado: sincronizacao
---

# dbo.CustomValorHistorico

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCus` | INT | não | sim | não |
| `idVal` | INT | não | sim | não |
| `dtAlteracao` | DATETIME | não | sim | não |
| `valorCus` | VARCHAR(4000) | não | não | não |
| `valorCusAntigo` | VARCHAR(4000) | não | não | não |
| `idUsu` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CustomValorHistorico` (idCus) → `dbo.Custom` (idCus)
