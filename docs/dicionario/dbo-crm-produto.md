---
gerado: sincronizacao
---

# dbo.CRM_Produto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idProd` | INT | não | sim | não |
| `dsProd` | VARCHAR(50) | não | não | não |
| `flgProdAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_ContratoItem` (idProd) → `dbo.CRM_Produto` (idProd)
