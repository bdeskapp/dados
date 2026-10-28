---
gerado: sincronizacao
---

# dbo.Cargo

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCar` | INT | não | sim | não |
| `dsCar` | VARCHAR(250) | sim | não | não |
| `flgCarAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioHierarquia` (idCar) → `dbo.Cargo` (idCar)
