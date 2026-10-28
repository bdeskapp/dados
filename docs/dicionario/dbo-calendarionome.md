---
gerado: sincronizacao
---

# dbo.CalendarioNome

**Selo:** Explicada

Explicada em:

- [calendário de atendimento](../dimensoes/tempo-calendario.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCan` | INT | não | sim | não |
| `dsCan` | VARCHAR(50) | não | não | não |
| `PadraoDia` | DECIMAL(15,2) | sim | não | não |
| `PadraoSemana` | DECIMAL(15,2) | sim | não | não |
| `flgCanAtivo` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_ContratoItem` (idCan) → `dbo.CalendarioNome` (idCan)
- `dbo.CalendarioNome` (idUsuOperacao) → `dbo.Usuario` (idUsu)
- `dbo.Calendario` (idCan) → `dbo.CalendarioNome` (idCan)
- `dbo.Grupo` (idCan) → `dbo.CalendarioNome` (idCan)
