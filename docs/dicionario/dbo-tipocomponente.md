---
gerado: sincronizacao
---

# dbo.TipoComponente

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpComp` | INT | não | sim | não |
| `dsTpComp` | VARCHAR(30) | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Atributo` (idTpComp) → `dbo.TipoComponente` (idTpComp)
- `dbo.InventarioConfig` (idTpCompMonitor) → `dbo.TipoComponente` (idTpComp)
- `dbo.InventarioConfig` (idTpCompSoft) → `dbo.TipoComponente` (idTpComp)
