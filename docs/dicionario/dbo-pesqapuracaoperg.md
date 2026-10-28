---
gerado: sincronizacao
---

# dbo.PesqApuracaoPerg

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesqApu` | INT | não | sim | não |
| `idPergunta` | INT | não | sim | não |
| `nTot` | INT | não | não | não |
| `nTotAbstencao` | INT | não | não | não |
| `nPercPart` | REAL | não | não | não |
| `nPercAbstencao` | REAL | não | não | não |
| `nResult` | REAL | não | não | não |

## Chaves estrangeiras

- `dbo.PesqApuracaoOpc` (idPesqApu, idPergunta) → `dbo.PesqApuracaoPerg` (idPesqApu, idPergunta)
- `dbo.PesqApuracaoPerg` (idPesqApu) → `dbo.PesqApuracao` (idPesqApu)
- `dbo.PesqApuracaoPerg` (idPergunta) → `dbo.PesqPergunta` (idPergunta)
