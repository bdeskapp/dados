---
gerado: sincronizacao
---

# dbo.KBStatus

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAre` | INT | não | sim | não |
| `cdKBClas` | CHAR(3) | não | sim | não |
| `cdKBSta` | CHAR(3) | não | sim | não |
| `dsKBSta` | VARCHAR(30) | não | não | não |
| `tpOper` | TINYINT | não | não | não |
| `flgConsulta` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.KBStatus` (idAre, cdKBClas) → `dbo.KBClasse` (idAre, cdKBClas)
- `dbo.KBase` (idAre, cdKBClas, cdKBSta) → `dbo.KBStatus` (idAre, cdKBClas, cdKBSta)
