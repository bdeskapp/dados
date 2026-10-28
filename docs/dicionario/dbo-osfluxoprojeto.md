---
gerado: sincronizacao
---

# dbo.OSFluxoProjeto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlo` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |
| `dtPlanejamento` | DATETIME | não | sim | não |
| `dtIniPrev` | DATETIME | sim | não | não |
| `dtFimPrev` | DATETIME | sim | não | não |
| `idUsu` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.OSFluxoProjeto` (idFlo, idTar) → `dbo.OsFluxo` (idFlO, idTar)
- `dbo.OSFluxoProjeto` (idUsu) → `dbo.Usuario` (idUsu)
