---
gerado: sincronizacao
---

# dbo.PatrimonioSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatSol` | INT | não | sim | não |
| `dtSolicitacao` | DATETIME | não | não | não |
| `idReq` | INT | não | não | não |
| `idReqPart` | INT | não | não | não |
| `idUsuSol` | INT | não | não | não |
| `idPatOp` | INT | não | não | não |
| `idPat` | INT | não | não | não |
| `dsColuna` | VARCHAR(50) | não | não | não |
| `valorSol` | VARCHAR(250) | sim | não | não |
| `flgEfetivar` | BIT | não | não | não |
| `dsLogErro` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.PatrimonioSolicitacao` (idPatOp) → `dbo.PatOperacao` (idPatOp)
- `dbo.PatrimonioSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatrimonioSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
