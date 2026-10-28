---
gerado: sincronizacao
---

# dbo.PatOpClasse

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatOp` | INT | não | sim | não |
| `idClas` | INT | não | sim | não |
| `flgAplica` | BIT | não | não | não |
| `flgRef` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.PatOpClasse` (idClas) → `dbo.Classe` (idClas)
- `dbo.PatOpClasse` (idPatOp) → `dbo.PatOperacao` (idPatOp)
