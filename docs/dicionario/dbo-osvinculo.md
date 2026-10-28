---
gerado: sincronizacao
---

# dbo.OSVinculo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOS` | INT | não | sim | não |
| `idOSVinculada` | INT | não | sim | não |
| `idOri` | INT | não | sim | não |
| `idTpVnc` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.OSVinculo` (idOri) → `dbo.Origem` (idOri)
- `dbo.OSVinculo` (idTpVnc) → `dbo.TipoOSVinculo` (IdTpVnc)
