---
gerado: sincronizacao
---

# dbo.RepSave

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPesquisa` | INT | não | sim | não |
| `idEntidade` | INT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtCreate` | DATETIME | não | não | não |
| `dsTitulo` | VARCHAR(100) | não | não | não |
| `tpAcesso` | CHAR(3) | não | não | não |
| `msgRodape` | VARCHAR(100) | sim | não | não |
| `flgQuebraTexto` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.RepPesquisaAgendada` (idPesquisa) → `dbo.RepSave` (idPesquisa)
- `dbo.RepSaveCond` (idPesquisa) → `dbo.RepSave` (idPesquisa)
- `dbo.RepSaveFields` (idPesquisa) → `dbo.RepSave` (idPesquisa)
- `dbo.RepSave` (idEntidade) → `dbo.RepEntidade` (idEntidade)
- `dbo.RepSave` (idUsu) → `dbo.Usuario` (idUsu)
