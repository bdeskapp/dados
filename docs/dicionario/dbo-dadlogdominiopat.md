---
gerado: sincronizacao
---

# dbo.DadLogDominioPat

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPat` | INT | não | sim | não |
| `idDadConPat` | INT | não | sim | não |
| `dtAlteracao` | DATETIME | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadLogDominioPat` (idPat, idDadConPat, dtAlteracao) → `dbo.DadLogPat` (idPat, idDadConPat, dtAlteracao)
