---
gerado: sincronizacao
---

# dbo.InventarioConfigDA

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `nmCampoInventario` | VARCHAR(50) | não | sim | não |
| `idDad` | INT | não | não | não |
| `idCon` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.InventarioConfigDA` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.InventarioConfigDA` (idDad) → `dbo.DadoAdicional` (idDad)
