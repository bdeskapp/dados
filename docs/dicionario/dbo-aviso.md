---
gerado: sincronizacao
---

# dbo.Aviso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAvi` | INT | não | sim | não |
| `dsAvi` | VARCHAR(50) | não | não | não |
| `idGru` | INT | sim | não | não |
| `flgAviAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Aviso` (idGru) → `dbo.Grupo` (idGru)
- `dbo.OS` (idAvi) → `dbo.Aviso` (idAvi)
