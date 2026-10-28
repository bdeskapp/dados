---
gerado: sincronizacao
---

# dbo.CRM_Gestor

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGestor` | INT | não | sim | não |
| `idUni` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.CRM_Gestor` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_Gestor` (idGestor) → `dbo.Usuario` (idUsu)
