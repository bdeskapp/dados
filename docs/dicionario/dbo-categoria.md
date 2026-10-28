---
gerado: sincronizacao
---

# dbo.Categoria

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCat` | INT | não | sim | não |
| `dsCat` | VARCHAR(100) | sim | não | não |
| `flgCatAtivo` | BIT | não | não | não |
| `idAre` | INT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Categoria` (idAre) → `dbo.Area` (idAre)
- `dbo.DadContextoCampo` (idCat) → `dbo.Categoria` (idCat)
- `dbo.FormCategoria` (idCat) → `dbo.Categoria` (idCat)
- `dbo.SubCategoria` (idCat) → `dbo.Categoria` (idCat)
- `dbo.Tarefa` (idCat) → `dbo.Categoria` (idCat)
