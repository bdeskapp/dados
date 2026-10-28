---
gerado: sincronizacao
---

# dbo.TipoPatrimonio

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [CMDB (itens de configuração e patrimônio)](../fora-de-escopo/cmdb.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpp` | INT | não | sim | não |
| `idClas` | INT | não | não | não |
| `dsTpp` | VARCHAR(50) | não | não | não |
| `flgTppAtivo` | BIT | não | não | não |
| `flgRelUsu` | BIT | não | não | não |
| `flgRelComp` | BIT | não | não | não |
| `flgRelGru` | BIT | não | não | não |
| `dsIcone` | VARCHAR(50) | não | não | não |
| `idGruAdm` | INT | sim | não | não |
| `tpEnvio` | TINYINT | não | não | não |
| `flgAlertaGru` | BIT | não | não | não |
| `flgAlertaUsu` | BIT | não | não | não |
| `tpCampoObrigatorio` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.FormPapelPatDom` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.InventarioConfigOp` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.KBPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.ListaICClasseTipo` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.MarcaTipoPat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.MetricaCalc_Pat` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.PatAlertaResumo` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.PatAlerta` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.Patrimonio` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.TipoPatrimonioRel` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.TipoPatrimonioRel` (idTppRel) → `dbo.TipoPatrimonio` (idTpp)
- `dbo.TipoPatrimonio` (idClas) → `dbo.Classe` (idClas)
- `dbo.TipoPatrimonio` (idGruAdm) → `dbo.Grupo` (idGru)
