---
gerado: sincronizacao
---

# dbo.Classe

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idClas` | INT | não | sim | não |
| `nmClas` | VARCHAR(50) | não | não | não |
| `flgClasAtivo` | BIT | não | não | não |
| `flgAssetHW` | SMALLINT | sim | não | não |
| `flgAssetSW` | SMALLINT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadContextoPat` (idClas) → `dbo.Classe` (idClas)
- `dbo.FormPapelPatDom` (idClas) → `dbo.Classe` (idClas)
- `dbo.InventarioConfig` (idClasMonitor) → `dbo.Classe` (idClas)
- `dbo.ListaICClasseTipo` (idClas) → `dbo.Classe` (idClas)
- `dbo.PatOpClasse` (idClas) → `dbo.Classe` (idClas)
- `dbo.StatusPatrimonio` (idClas) → `dbo.Classe` (idClas)
- `dbo.TipoPatrimonio` (idClas) → `dbo.Classe` (idClas)
