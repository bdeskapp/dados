---
gerado: sincronizacao
---

# dbo.DadValorPatSolicitacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadValPatSol` | INT | não | sim | não |
| `idPat` | INT | não | não | não |
| `idReq` | INT | não | não | não |
| `idDadConPat` | INT | não | não | não |
| `idUsuSol` | INT | não | não | não |
| `dtSolicitacao` | DATETIME | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `numero` | DECIMAL(17,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |
| `flgEfetivar` | BIT | não | não | não |
| `dsLogErro` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.DadValorDominioPatSolicitacao` (idDadValPatSol) → `dbo.DadValorPatSolicitacao` (idDadValPatSol)
- `dbo.DadValorPatSolicitacao` (idDadConPat) → `dbo.DadContextoPat` (idDadConPat)
- `dbo.DadValorPatSolicitacao` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.DadValorPatSolicitacao` (idUsuSol) → `dbo.Usuario` (idUsu)
