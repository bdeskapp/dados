---
gerado: sincronizacao
---

# dbo.MonitorConfigAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMonitor` | INT | não | sim | não |
| `idUsu` | INT | não | não | não |
| `idGru` | INT | sim | não | não |
| `tpPart` | TINYINT | não | não | não |
| `flgReg` | BIT | não | não | não |
| `flgDir` | BIT | não | não | não |
| `flgAcao` | BIT | não | não | não |
| `flgResumo` | BIT | não | não | não |
| `flgVip` | BIT | não | não | não |
| `flgPriAlta` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.MonitorConfigAlerta` (idGru) → `dbo.Grupo` (idGru)
- `dbo.MonitorConfigAlerta` (idUsu) → `dbo.Usuario` (idUsu)
