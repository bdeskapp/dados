---
gerado: sincronizacao
---

# dbo.RepPesquisaAgendada

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `dtInicial` | DATETIME | sim | não | não |
| `dtFinal` | DATETIME | sim | não | não |
| `flgRecorrencia` | CHAR(1) | não | não | não |
| `flgUltDiaMes` | BIT | sim | não | não |
| `dtUltExecucao` | DATETIME | sim | não | não |
| `flgAcessoAutor` | BIT | não | não | não |
| `flgDiaUtil` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.RepPesquisaAgendadaUsu` (idPesquisa) → `dbo.RepPesquisaAgendada` (idPesquisa)
- `dbo.RepPesquisaAgendada` (idPesquisa) → `dbo.RepSave` (idPesquisa)
