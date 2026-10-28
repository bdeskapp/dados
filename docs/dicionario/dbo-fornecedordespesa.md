---
gerado: sincronizacao
---

# dbo.FornecedorDespesa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFornecedor` | INT | não | sim | não |
| `idCatDesp` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FornecedorDespesa` (idCatDesp) → `dbo.CategoriaDespesa` (idCatDesp)
- `dbo.FornecedorDespesa` (idFornecedor) → `dbo.Empresa` (idEmp)
