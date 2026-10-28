---
gerado: sincronizacao
---

# dbo.DadContextoDesd

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idFrmRel` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoDesd` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
