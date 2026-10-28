---
gerado: sincronizacao
---

# dbo.RepCampos

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCampo` | INT | não | sim | não |
| `Descricao` | VARCHAR(50) | sim | não | não |
| `TipoDado` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.RepDetCampos` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepSaveCond` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepSaveFields` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepWorkCond` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepWorkFields` (idCampo) → `dbo.RepCampos` (idCampo)
