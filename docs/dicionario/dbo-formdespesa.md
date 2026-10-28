---
gerado: sincronizacao
---

# dbo.FormDespesa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `idCatDesp` | INT | não | sim | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.FormDespesa` (idFrm) → `dbo.Formulario` (idFrm)
