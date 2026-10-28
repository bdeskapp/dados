---
gerado: sincronizacao
---

# dbo.CRM_FatAcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUni` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |

## Chaves estrangeiras

- `dbo.CRM_FatAcesso` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_FatAcesso` (idUsu) → `dbo.Usuario` (idUsu)
