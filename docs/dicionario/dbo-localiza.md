---
gerado: sincronizacao
---

# dbo.Localiza

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idLoc` | INT | não | sim | não |
| `idLocNiv` | INT | não | não | não |
| `dsLoc` | VARCHAR(100) | não | não | não |
| `dsLocComp` | VARCHAR(1200) | sim | não | não |
| `sigla` | VARCHAR(5) | sim | não | não |
| `idLocAsc` | INT | sim | não | não |
| `dtIniLoc` | DATETIME | não | não | não |
| `dtFimLoc` | DATETIME | sim | não | não |
| `idLocAscSemNull` | computada | sim | não | sim |

## Chaves estrangeiras

- `dbo.AgendaReq` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.CompAlertaMinimo` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.CompEstoque` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.CompMovimento` (idLocE) → `dbo.Localiza` (idLoc)
- `dbo.CompMovimento` (idLocS) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteAlerta` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteLocal` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteMovimento` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.ComponenteMovimento` (idLocDest) → `dbo.Localiza` (idLoc)
- `dbo.Localiza` (idLocNiv) → `dbo.LocNivel` (idLocNiv)
- `dbo.Localiza` (idLocAsc) → `dbo.Localiza` (idLoc)
- `dbo.MetricaCalc_Pat` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.OS` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.PatMovimento` (idLocAnt) → `dbo.Localiza` (idLoc)
- `dbo.PatMovimento` (idLocAtual) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAssociadoSolicitacao` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAtributoSolicitacao` (idLocE) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioAtributoSolicitacao` (idLocS) → `dbo.Localiza` (idLoc)
- `dbo.PatrimonioMovimento` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Patrimonio` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Req` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.UsuarioPatrimonioSolicitacao` (idLoc) → `dbo.Localiza` (idLoc)
- `dbo.Usuario` (idLoc) → `dbo.Localiza` (idLoc)
