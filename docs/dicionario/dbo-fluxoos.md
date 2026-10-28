---
gerado: sincronizacao
---

# dbo.FluxoOS

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlO` | INT | não | sim | não |
| `idFlu` | INT | não | não | não |
| `SLAFluxo` | REAL | sim | não | não |
| `FlgStaFlu` | TINYINT | não | não | não |
| `dsTitulo` | VARCHAR(100) | sim | não | não |
| `idTarAtual` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.FluxoOS` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.FluxoOsAnexo` (idFlo) → `dbo.FluxoOS` (idFlO)
- `dbo.OS` (idFlO) → `dbo.FluxoOS` (idFlO)
- `dbo.OsFluxo` (idFlO) → `dbo.FluxoOS` (idFlO)
