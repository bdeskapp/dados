---
gerado: sincronizacao
---

# dbo.CategoriaProcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCatProc` | SMALLINT | não | sim | não |
| `dsCatProc` | VARCHAR(30) | não | não | não |
| `idAre` | INT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CategoriaProcesso` (idAre) → `dbo.Area` (idAre)
- `dbo.Formulario` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.Processo` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.TagCardapio_CategoriaProcesso` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
- `dbo.UsuarioCategoria_ItemCardapio` (idCatProc) → `dbo.CategoriaProcesso` (idCatProc)
