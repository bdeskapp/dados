---
gerado: sincronizacao
---

# dbo.Objeto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idObj` | INT | não | sim | não |
| `nmObj` | VARCHAR(255) | sim | não | não |
| `dsObj` | VARCHAR(50) | não | não | não |
| `menu` | VARCHAR(2) | sim | não | não |
| `dep` | INT | sim | não | não |
| `cliente` | VARCHAR(50) | sim | não | não |
| `tpObj` | CHAR(3) | não | não | não |
| `idMod` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.AcessoRapido` (idObj) → `dbo.Objeto` (idObj)
- `dbo.FAQObjeto` (idObj) → `dbo.Objeto` (idObj)
- `dbo.Favoritos` (idObj) → `dbo.Objeto` (idObj)
- `dbo.PerfilObjeto` (idObj) → `dbo.Objeto` (idObj)
- `dbo.Perfil` (idObjDefault) → `dbo.Objeto` (idObj)
- `dbo.Usuario` (idObjDefault) → `dbo.Objeto` (idObj)
