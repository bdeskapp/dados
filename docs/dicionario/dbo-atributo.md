---
gerado: sincronizacao
---

# dbo.Atributo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAtr` | INT | não | sim | não |
| `dsAtr` | VARCHAR(60) | não | não | não |
| `idUnm` | INT | sim | não | não |
| `flgAtrAtivo` | BIT | não | não | não |
| `idTpComp` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.Atributo` (idTpComp) → `dbo.TipoComponente` (idTpComp)
- `dbo.Atributo` (idUnm) → `dbo.UnidadeMedida` (idUnm)
- `dbo.CompAlertaMinimo` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.CompEstoque` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.CompMovimento` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteAlerta` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteLocal` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.ComponenteMovimento` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.PatrimonioAtributoSolicitacao` (idAtr) → `dbo.Atributo` (idAtr)
- `dbo.PatrimonioAtributo` (idAtr) → `dbo.Atributo` (idAtr)
