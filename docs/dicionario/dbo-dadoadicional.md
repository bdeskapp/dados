---
gerado: sincronizacao
---

# dbo.DadoAdicional

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDad` | INT | não | sim | não |
| `dsDad` | VARCHAR(100) | sim | não | não |
| `dsComplementar` | VARCHAR(1000) | sim | não | não |
| `observacao` | VARCHAR(250) | sim | não | não |
| `tpDado` | TINYINT | não | não | não |
| `tpApresentacao` | TINYINT | não | não | não |
| `TamMax` | INT | sim | não | não |
| `idView` | INT | sim | não | não |
| `nmCampoView` | VARCHAR(50) | sim | não | não |
| `flgDadAtivo` | BIT | não | não | não |
| `flgExibeLista` | BIT | sim | não | não |
| `flgExibeFiltro` | BIT | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgControle` | BIT | não | não | não |
| `idDadPai` | INT | sim | não | não |
| `idAcao` | INT | sim | não | não |
| `tpValidacao` | VARCHAR(10) | sim | não | não |
| `idStoreProc` | INT | sim | não | não |
| `intervaloData` | VARCHAR(10) | sim | não | não |

## Chaves estrangeiras

- `dbo.DadColecao` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadCondicao` (idDadCond) → `dbo.DadoAdicional` (idDad)
- `dbo.DadCondicao` (idDadAfetado) → `dbo.DadoAdicional` (idDad)
- `dbo.DadContextoCampo` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadContextoPat` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadDominio` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicionalUsuarioLog` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicionalUsuario` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicional` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.DadoAdicional` (idView) → `dbo.DadDominioTabela` (idView)
- `dbo.DadoAdicional` (idDadPai) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicional` (idStoreProc) → `dbo.DadStoreProcedure` (idStoreProc)
- `dbo.InventarioConfigDA` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.PerfilAcessoCargoSistema` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepSaveCond` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepSaveFields` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepWorkCond` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.RepWorkFields` (idDad) → `dbo.DadoAdicional` (idDad)
