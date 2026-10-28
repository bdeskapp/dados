---
gerado: sincronizacao
---

# dbo.CategoriaDespesa

**Selo:** Explicada

Explicada em:

- [apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCatDesp` | INT | não | sim | não |
| `dsCatDesp` | VARCHAR(30) | não | não | não |
| `flgCatAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgFornObrigatorio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.FornecedorDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.ItemDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.ReqDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
