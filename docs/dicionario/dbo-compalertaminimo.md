---
gerado: sincronizacao
---

# dbo.CompAlertaMinimo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCompMin` | INT | não | sim | não |
| `idAtr` | INT | não | não | não |
| `idLoc` | INT | sim | não | não |
| `qtdMin` | INT | não | não | não |
| `tpAlerta` | CHAR(1) | sim | não | não |

## Chaves estrangeiras

- `dbo.CompAlertaMinimo` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.CompAlertaMinimo` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.CompAlertaNotifica` (idCompMin) → `dbo.CompAlertaMinimo` (idCompMin)
