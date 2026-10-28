---
gerado: sincronizacao
---

# dbo.CompEstoque

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAtr` | INT | não | sim | não |
| `idLoc` | INT | não | sim | não |
| `idStatus` | INT | não | sim | não |
| `qtdTotal` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CompEstoque` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.CompEstoque` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.CompEstoque` (idStatus) → `dbo.StatusPatrimonio` (idStatusPat)
