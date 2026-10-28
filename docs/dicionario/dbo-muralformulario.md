---
gerado: sincronizacao
---

# dbo.MuralFormulario

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMural` | INT | não | sim | não |
| `idFormulario` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.MuralFormulario` (idFormulario) → `dbo.Formulario` (idFrm)
- `dbo.MuralFormulario` (idMural) → `dbo.Mural` (idMural)
