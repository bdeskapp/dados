---
gerado: sincronizacao
---

# dbo.CondCamposImpactoNivel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idImp` | INT | não | sim | não |
| `nImpNivel` | INT | não | sim | não |
| `idFrm` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.CondCamposImpactoNivel` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondCamposImpactoNivel` (idImp, nImpNivel) → `dbo.ImpactoNivel` (idImp, nImpNivel)
