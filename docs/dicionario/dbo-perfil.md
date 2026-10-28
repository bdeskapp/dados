---
gerado: sincronizacao
---

# dbo.Perfil

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPer` | INT | não | sim | não |
| `nmPer` | VARCHAR(20) | não | não | não |
| `dsPer` | VARCHAR(100) | não | não | não |
| `idObjDefault` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.PerfilCampoLayout` (idPer) → `dbo.Perfil` (idPer)
- `dbo.PerfilFavorito` (idPer) → `dbo.Perfil` (idPer)
- `dbo.PerfilObjeto` (idPer) → `dbo.Perfil` (idPer)
- `dbo.Perfil` (idObjDefault) → `dbo.Objeto` (idObj)
- `dbo.ProfileObject` (ProfileID) → `dbo.Perfil` (idPer)
- `dbo.Profile_Item` (idProfile) → `dbo.Perfil` (idPer)
- `dbo.RelCustPerfil` (idPer) → `dbo.Perfil` (idPer)
- `dbo.SyncUsuConfig` (idPer) → `dbo.Perfil` (idPer)
- `dbo.Usuario` (idPer) → `dbo.Perfil` (idPer)
