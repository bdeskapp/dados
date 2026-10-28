---
gerado: sincronizacao
---

# dbo.RelacaoEfeito

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idRel` | INT | não | não | não |
| `flgEval` | BIT | não | não | não |
| `nSeq` | SMALLINT | não | não | não |
| `flgRepeat` | BIT | não | não | não |
| `tpEfeito` | CHAR(1) | não | não | não |
| `idFrmStatus` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.Efeito` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoAcao` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoAlerta` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoAtribuicao` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoEfeito` (idFrmStatus) → `dbo.FormStatus` (idFrmStatus)
- `dbo.RelacaoEfeito` (idRel) → `dbo.Relacao` (idRel)
