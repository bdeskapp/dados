---
gerado: sincronizacao
---

# dbo.RepPesquisaAgendadaUsu

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RepPesquisaAgendadaUsu` (idPesquisa) → `dbo.RepPesquisaAgendada` (idPesquisa)
- `dbo.RepPesquisaAgendadaUsu` (idUsu) → `dbo.Usuario` (idUsu)
