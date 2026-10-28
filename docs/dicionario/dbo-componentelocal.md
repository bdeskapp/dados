---
gerado: sincronizacao
---

# dbo.ComponenteLocal

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLoc` | INT | sim | não | não |
| `idAtr` | INT | não | não | não |
| `qtdMinCmp` | CHAR(18) | sim | não | não |
| `idStatusPat` | INT | sim | não | não |
| `qtdTotalCmp` | INT | sim | não | não |
| `frqAlertaCmp` | VARCHAR(20) | sim | não | não |
| `flgEmailEnviado` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.ComponenteLocal` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteLocal` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteLocal` (idStatusPat) → `dbo.StatusPatrimonio` (idStatusPat)
