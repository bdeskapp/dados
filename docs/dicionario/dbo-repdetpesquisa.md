---
gerado: sincronizacao
---

# dbo.RepDetPesquisa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `idCampo` | INT | não | sim | não |
| `intSelecao` | INT | não | não | não |
| `sCondicoes` | VARCHAR(2000) | sim | não | não |
| `sDescCondicoes` | VARCHAR(2000) | sim | não | não |
| `intOrdem` | INT | não | não | não |
| `sTotalizar` | VARCHAR(255) | sim | não | não |
| `idDad` | INT | sim | não | não |
| `idCon` | INT | sim | não | não |
| `flgFluxo` | BIT | sim | não | não |

## Chaves estrangeiras

- `dbo.RepDetPesquisa` (idPesquisa) → `dbo.RepPesquisa` (idPesquisa)
