---
gerado: sincronizacao
---

# dbo.Status

**Selo:** Explicada

Explicada em:

- [status](../dimensoes/status-fase.md)
- [tempo por status](../fatos/tempo-por-status.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSta` | INT | não | sim | não |
| `dsSta` | VARCHAR(30) | não | não | não |
| `flgStaAtivo` | BIT | não | não | não |
| `cdSta` | VARCHAR(6) | sim | não | não |
| `flgFormulario` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormStatus` (idSta) → `dbo.Status` (idSta)
- `dbo.OS` (idSta) → `dbo.Status` (idSta)
