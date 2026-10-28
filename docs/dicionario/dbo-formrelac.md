---
gerado: sincronizacao
---

# dbo.FormRelac

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmRel` | INT | não | sim | não |
| `idFrm` | INT | não | não | não |
| `idFrmRelac` | INT | não | não | não |
| `cdVinc` | CHAR(5) | não | não | não |
| `idTpVinculo` | INT | não | não | não |
| `tpQuebra` | CHAR(1) | não | não | não |
| `flgDepende` | BIT | não | não | não |
| `flgStatus` | BIT | não | não | não |
| `flgCompleta` | BIT | não | não | não |
| `flgAssunto` | BIT | não | não | não |
| `flgDescricao` | BIT | não | não | não |
| `flgOrigem` | BIT | não | não | não |
| `flgLocaliza` | BIT | não | não | não |
| `flgAtividade` | BIT | não | não | não |
| `flgPrioridade` | BIT | não | não | não |
| `flgImpacto` | BIT | não | não | não |
| `flgUrgencia` | BIT | não | não | não |
| `flgANTE` | BIT | não | não | não |
| `flgBEN` | BIT | não | não | não |
| `flgADO` | BIT | não | não | não |
| `flgADM` | BIT | não | não | não |
| `flgOutros` | BIT | não | não | não |
| `tpDad` | CHAR(1) | sim | não | não |
| `flgCompartilhaAnexo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormRelacAcao` (idFrmRel) → `dbo.FormRelac` (idFrmRel)
- `dbo.FormRelacStatus` (idFrmRel) → `dbo.FormRelac` (idFrmRel)
- `dbo.FormRelac` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormRelac` (idFrmRelac) → `dbo.Formulario` (idFrm)
- `dbo.FormRelac` (idTpVinculo) → `dbo.TipoVinculo` (idTpVinculo)
- `dbo.FormRelac` (cdVinc) → `dbo.Vinculo` (cdVinc)
