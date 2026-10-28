---
gerado: sincronizacao
---

# dbo.InventarioConfig

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUnm` | INT | não | não | não |
| `idTpCompSoft` | INT | sim | não | não |
| `flgMonitorComp` | BIT | não | não | não |
| `flgMonitorPat` | BIT | não | não | não |
| `idTpCompMonitor` | INT | sim | não | não |
| `idClasMonitor` | INT | sim | não | não |
| `tempoLog` | TINYINT | não | não | não |
| `idUsu1` | INT | não | não | não |
| `idUsu2` | INT | sim | não | não |
| `idUsu3` | INT | sim | não | não |
| `idFrm` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.InventarioConfig` (idClasMonitor) → `dbo.Classe` (idClas)
- `dbo.InventarioConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.InventarioConfig` (idTpCompMonitor) → `dbo.TipoComponente` (idTpComp)
- `dbo.InventarioConfig` (idTpCompSoft) → `dbo.TipoComponente` (idTpComp)
- `dbo.InventarioConfig` (idUnm) → `dbo.UnidadeMedida` (idUnm)
- `dbo.InventarioConfig` (idUsu1) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idUsu2) → `dbo.Usuario` (idUsu)
- `dbo.InventarioConfig` (idUsu3) → `dbo.Usuario` (idUsu)
