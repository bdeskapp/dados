---
gerado: sincronizacao
---

# dbo.DadStoreProcedure

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idStoreProc` | INT | não | sim | não |
| `nmStoreProc` | VARCHAR(100) | não | não | não |
| `flgStoreProcAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadoAdicional` (idStoreProc) → `dbo.DadStoreProcedure` (idStoreProc)
