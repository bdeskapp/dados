---
gerado: sincronizacao
---

# dbo.Area

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)
- [grupo e área](../dimensoes/grupo-area.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAre` | INT | não | sim | não |
| `dsAre` | VARCHAR(30) | sim | não | não |
| `nmBanco` | VARCHAR(30) | não | não | não |
| `flgAreaAtiva` | BIT | não | não | não |
| `flgBancoPrincipal` | BIT | sim | não | não |
| `idGruAdm` | INT | sim | não | não |
| `idGruKB` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.Area` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.Area` (idGruKB) → `dbo.Grupo` (idGru)
- `dbo.CategoriaProcesso` (idAre) → `dbo.Area` (idAre)
- `dbo.Categoria` (idAre) → `dbo.Area` (idAre)
- `dbo.ComponenteMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.DadContextoCampo` (idAre) → `dbo.Area` (idAre)
- `dbo.FluxoTarefa` (idAre) → `dbo.Area` (idAre)
- `dbo.Formulario` (idAre) → `dbo.Area` (idAre)
- `dbo.Grupo` (idAre) → `dbo.Area` (idAre)
- `dbo.KBClasse` (idAre) → `dbo.Area` (idAre)
- `dbo.KBase` (idAre) → `dbo.Area` (idAre)
- `dbo.LicencaMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.MetricaCalc_Are` (idAre) → `dbo.Area` (idAre)
- `dbo.MetricaCalc_Hie` (idAre) → `dbo.Area` (idAre)
- `dbo.OsFluxo` (idAre) → `dbo.Area` (idAre)
- `dbo.PatrimonioMovimento` (idARE) → `dbo.Area` (idAre)
- `dbo.Processo` (idAre) → `dbo.Area` (idAre)
- `dbo.RepAcesso` (idAre) → `dbo.Area` (idAre)
- `dbo.Req` (idAre) → `dbo.Area` (idAre)
- `dbo.UsuarioExterno` (idAre) → `dbo.Area` (idAre)
- `dbo.VIP` (idAre) → `dbo.Area` (idAre)
