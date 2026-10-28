---
gerado: sincronizacao
---

# dbo.PatOperacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatOp` | INT | não | sim | não |
| `dsPatOp` | VARCHAR(50) | não | não | não |
| `tpPatOp` | CHAR(1) | não | não | não |
| `flgCad` | BIT | não | não | não |
| `flgReq` | BIT | não | não | não |
| `flgAplicComp` | BIT | não | não | não |
| `flgRefUsu` | BIT | não | não | não |
| `flgEstoque` | BIT | não | não | não |
| `flgTemp` | BIT | não | não | não |
| `flgStatus` | BIT | não | não | não |
| `flgLoc` | BIT | não | não | não |
| `idPatRel` | INT | sim | não | não |
| `idStatus` | INT | sim | não | não |
| `flgAtivo` | BIT | não | não | não |
| `idFrm` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `flgDefault` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CompMovimento` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAjuste) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssComp) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssMon) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpAssSoft) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissComp) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissMon) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpDissSoft) → `dbo.PatOperacao` (idPatOp)
- `dbo.InventarioConfigOp` (idPatOpEntrada) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatAlerta` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatMovimento` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatOpClasse` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatOpQPOQQ` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatOperacao` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.PatOperacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatOperacao` (idStatus) → `dbo.StatusPatrimonio` (idStatusPat)
- `dbo.PatOperacao` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatrimonioAtributoSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatrimonioSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.UsuarioPatrimonioSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
