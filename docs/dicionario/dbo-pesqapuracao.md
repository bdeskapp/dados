---
gerado: sincronizacao
---

# dbo.PesqApuracao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesqApu` | INT | não | sim | não |
| `idPesq` | INT | não | não | não |
| `dtTermino` | DATETIME | não | não | não |
| `nTot` | INT | não | não | não |
| `nTotPrevisto` | INT | não | não | não |
| `nResult` | REAL | não | não | não |
| `dtInicio` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.PesqApuracaoPerg` (idPesqApu) → `dbo.PesqApuracao` (idPesqApu)
- `dbo.PesqApuracao` (idPesq) → `dbo.Pesquisa` (idPesq)
