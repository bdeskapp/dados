---
gerado: sincronizacao
---

# dbo.Calendario

**Selo:** Explicada

Explicada em:

- [calendário de atendimento](../dimensoes/tempo-calendario.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCan` | INT | não | não | não |
| `idCal` | INT | não | sim | não |
| `diaSemana` | INT | sim | não | não |
| `dtCal` | DATETIME | sim | não | não |
| `hInicio1` | VARCHAR(5) | sim | não | não |
| `hFim1` | VARCHAR(5) | sim | não | não |
| `hInicio2` | VARCHAR(5) | sim | não | não |
| `hFim2` | VARCHAR(5) | sim | não | não |
| `hInicio3` | VARCHAR(5) | sim | não | não |
| `hFim3` | VARCHAR(5) | sim | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.Calendario` (idCan) → `dbo.CalendarioNome` (idCan)
- `dbo.Calendario` (idUsuOperacao) → `dbo.Usuario` (idUsu)
