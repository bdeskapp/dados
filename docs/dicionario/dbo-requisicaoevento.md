---
gerado: sincronizacao
---

# dbo.RequisicaoEvento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEvento` | INT | não | sim | não |
| `tipo` | VARCHAR(20) | não | não | não |
| `dtEvento` | DATETIME | não | não | não |
| `idReqHist` | INT | sim | não | não |
| `idReqLog` | INT | sim | não | não |
| `idDadLog` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.EnvioSistemaExterno` (idEvento) → `dbo.RequisicaoEvento` (idEvento)
- `dbo.RequisicaoEvento` (idDadLog) → `dbo.DadLog` (idDadLog)
- `dbo.RequisicaoEvento` (idReqLog) → `dbo.RequisicaoLog` (idReqLog)
