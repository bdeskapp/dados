---
gerado: sincronizacao
---

# dbo.PerfilObjeto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPer` | INT | não | sim | não |
| `idObj` | INT | não | sim | não |
| `tpAcesso` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.PerfilObjeto` (idObj) → `dbo.Objeto` (idObj)
- `dbo.PerfilObjeto` (idPer) → `dbo.Perfil` (idPer)
