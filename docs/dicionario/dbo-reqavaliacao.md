---
gerado: sincronizacao
---

# dbo.ReqAvaliacao

**Selo:** Explicada

Explicada em:

- [avaliação e satisfação](../fatos/avaliacao-satisfacao.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `opAvaliacao` | TINYINT | sim | não | não |
| `dsAvaliacao` | TEXT | sim | não | não |
| `idUsu` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqAvaliacao` (idUsu) → `dbo.Usuario` (idUsu)
