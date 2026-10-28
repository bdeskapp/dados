---
gerado: sincronizacao
---

# dbo.Acao

**Selo:** Explicada

Explicada em:

- [ação](../dimensoes/acao.md)
- [eventos do histórico](../fatos/eventos-historico.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAcao` | INT | não | sim | não |
| `cdAcao` | VARCHAR(8) | não | não | não |
| `dsAcao` | VARCHAR(30) | não | não | não |
| `dsIcone` | VARCHAR(100) | sim | não | não |
| `flgFluxo` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |
| `flgAcaoAtiva` | BIT | não | não | não |
| `flgContexto` | BIT | não | não | não |
| `nGrupo` | TINYINT | sim | não | não |
| `nOrdem` | TINYINT | sim | não | não |
| `flgDado` | BIT | não | não | não |
| `flgSYS` | BIT | não | não | não |
| `flgRelacionaFaq` | BIT | não | não | não |
| `flgResp` | BIT | não | não | não |
| `tpHistorico` | CHAR(1) | não | não | não |
| `tpMotivo` | CHAR(1) | não | não | não |
| `tpDireta` | CHAR(1) | não | não | não |
| `tpInterna` | CHAR(1) | não | não | não |
| `flgTrans` | BIT | não | não | não |
| `flgTimeOut` | BIT | não | não | não |
| `flgNot` | BIT | não | não | não |
| `tpAbertura` | CHAR(1) | não | não | não |
| `flgConcluida` | BIT | não | não | não |
| `flgRelDado` | BIT | não | não | não |
| `tpLayout` | CHAR(1) | sim | não | não |
| `tpTimeOutManual` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.DadAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.DadoAdicional` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.FAQAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.FormAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.RotinaMapaVar` (idAcaoCopiaDescricao) → `dbo.Acao` (idAcao)
