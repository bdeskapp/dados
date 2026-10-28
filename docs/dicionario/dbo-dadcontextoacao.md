---
gerado: sincronizacao
---

# dbo.DadContextoAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `dsLink` | VARCHAR(100) | sim | não | não |
| `flgHide` | BIT | sim | não | não |
| `dsAlerta` | VARCHAR(100) | sim | não | não |

## Chaves estrangeiras

- `dbo.DadContextoAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
