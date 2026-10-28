---
gerado: sincronizacao
---

# dbo.ItemDespesa

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idItemDesp` | INT | não | sim | não |
| `idCatDesp` | INT | não | não | não |
| `dsItemDesp` | VARCHAR(30) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgItemAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ItemDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.ReqDespesa` (idItemDesp) → `dbo.ItemDespesa` (idItemDesp)
