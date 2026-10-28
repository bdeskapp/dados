---
gerado: sincronizacao
---

# dbo.CampoLayout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCampoL` | INT | não | sim | não |
| `nmObjL` | VARCHAR(50) | não | não | não |
| `nmCampoL` | VARCHAR(50) | não | não | não |
| `dsCampoL` | VARCHAR(50) | não | não | não |
| `Largura` | INT | não | não | não |
| `OrdemL` | INT | sim | não | não |
| `FlgDefault` | INT | não | não | não |
| `tpCampo` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioCampoLayout` (idCampoL) → `dbo.CampoLayout` (idCampoL)
