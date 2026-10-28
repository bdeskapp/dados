---
gerado: sincronizacao
---

# dbo.CRM_Segmento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSeg` | INT | não | sim | não |
| `dsSeg` | VARCHAR(50) | não | não | não |
| `flgSegAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_Empresa` (idSeg) → `dbo.CRM_Segmento` (idSeg)
