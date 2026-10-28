---
gerado: sincronizacao
---

# dbo.Divisao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDiv` | INT | não | sim | não |
| `dsDiv` | VARCHAR(100) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DivisaoGrupoAcesso` (idDiv) → `dbo.Divisao` (idDiv)
- `dbo.Empresa` (idDiv) → `dbo.Divisao` (idDiv)
