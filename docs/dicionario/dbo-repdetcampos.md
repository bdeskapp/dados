---
gerado: sincronizacao
---

# dbo.RepDetCampos

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCampo` | INT | não | sim | não |
| `idEntidade` | INT | não | sim | não |
| `Sequencia` | INT | não | sim | não |
| `NomeCampo` | VARCHAR(1500) | não | não | não |
| `Tabelas` | VARCHAR(455) | não | não | não |
| `Link` | VARCHAR(455) | não | não | não |
| `AliasSelect` | VARCHAR(1500) | não | não | não |
| `refFiltro` | VARCHAR(1500) | não | não | não |
| `OpcaoFiltro` | VARCHAR(2000) | não | não | não |
| `AliasGrupo` | VARCHAR(1500) | não | não | não |
| `flgDistinct` | INT | sim | não | não |
| `flgCorGrupo` | INT | sim | não | não |
| `idSecao` | INT | sim | não | não |
| `dsHelp` | VARCHAR(250) | sim | não | não |
| `dsHelpCond` | VARCHAR(250) | sim | não | não |

## Chaves estrangeiras

- `dbo.RepDetCampos` (idCampo) → `dbo.RepCampos` (idCampo)
- `dbo.RepDetCampos` (idEntidade) → `dbo.RepEntidade` (idEntidade)
- `dbo.RepDetCampos` (idSecao) → `dbo.RepSecao` (idSecao)
