---
gerado: sincronizacao
---

# dbo.Tabela

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTab` | INT | não | sim | não |
| `nmModulo` | VARCHAR(30) | não | não | não |
| `nmTab` | VARCHAR(30) | não | não | não |
| `flgAdmin` | BIT | não | não | não |
| `flgGestor` | BIT | não | não | não |
| `flgLog` | BIT | não | não | não |
| `flgCustom` | BIT | não | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |
| `nuDiasLog` | SMALLINT | não | não | não |
| `flgUsuario` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.TabelaAdmin` (idTab) → `dbo.Tabela` (idTab)
- `dbo.TabelaCompartilhada` (idTab) → `dbo.Tabela` (idTab)
- `dbo.TabelaLog` (idTab) → `dbo.Tabela` (idTab)
- `dbo.Tabela` (idTpPapel) → `dbo.TipoPapel` (idTpPapel)
