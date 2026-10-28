---
gerado: sincronizacao
---

# dbo.Papel

**Selo:** Explicada

Explicada em:

- [participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPapel` | INT | não | sim | não |
| `cdPapel` | VARCHAR(6) | sim | não | não |
| `dsPapel` | VARCHAR(50) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapel` (idPapel) → `dbo.Papel` (idPapel)
- `dbo.PapelTipoPapel` (idPapel) → `dbo.Papel` (idPapel)
