---
gerado: sincronizacao
---

# dbo.PatrimonioAtributo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatAtr` | INT | não | sim | não |
| `idPat` | INT | não | não | não |
| `idAtr` | INT | não | não | não |
| `valor` | VARCHAR(20) | não | não | não |
| `Qtde` | INT | não | não | não |
| `dtIniPatAtr` | DATETIME | não | não | não |
| `dtFimPatAtr` | DATETIME | sim | não | não |
| `idPatRel` | INT | não | não | não |
| `dtUltAlt` | DATETIME | sim | não | não |
| `dtValAssociacao` | DATETIME | sim | não | não |
| `idCompMovIni` | INT | sim | não | não |
| `idCompMovFim` | INT | sim | não | não |
| `idCompMovAlt` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioAtributo` (idCompMovIni) → `dbo.CompMovimento` (idCompMov)
- `dbo.PatrimonioAtributo` (idCompMovFim) → `dbo.CompMovimento` (idCompMov)
- `dbo.PatrimonioAtributo` (idCompMovAlt) → `dbo.CompMovimento` (idCompMov)
- `dbo.PatrimonioAtributo` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAtributo` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.PatrimonioAtributo` (idPat) → `dbo.Patrimonio` (idPat)
