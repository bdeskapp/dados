---
gerado: sincronizacao
---

# dbo.TipoMensagem

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpMsg` | INT | não | sim | não |
| `dsTpMsg` | VARCHAR(40) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqMensagem` (idTpMsg) → `dbo.TipoMensagem` (idTpMsg)
