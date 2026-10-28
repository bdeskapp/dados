---
gerado: sincronizacao
---

# dbo.AnaDetPesquisa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `Comparativo` | CHAR(1) | sim | não | não |
| `Visualizacao` | CHAR(1) | sim | não | não |
| `flgRegistrada` | BIT | sim | não | não |
| `flgConcluida` | BIT | sim | não | não |
| `flgPendente` | BIT | sim | não | não |
| `flgAgendada` | BIT | sim | não | não |
| `flgDentroForaSla` | BIT | sim | não | não |
| `flg10Mais` | BIT | sim | não | não |

## Chaves estrangeiras

- `dbo.AnaDetPesquisa` (idPesquisa) → `dbo.AnaPesquisa` (idPesquisa)
