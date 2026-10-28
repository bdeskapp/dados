---
gerado: sincronizacao
---

# dbo.TipoConclusao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpco` | INT | não | sim | não |
| `dsTpco` | VARCHAR(30) | não | não | não |
| `flgTpcoAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.OS` (idTpco) → `dbo.TipoConclusao` (idTpco)
