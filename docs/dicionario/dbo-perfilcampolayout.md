---
gerado: sincronizacao
---

# dbo.PerfilCampoLayout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPer` | INT | não | sim | não |
| `idCampoL` | INT | não | sim | não |
| `usuOrdemL` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.PerfilCampoLayout` (idPer) → `dbo.Perfil` (idPer)
