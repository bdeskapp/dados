---
gerado: sincronizacao
---

# dbo.FormCategoria

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `idCat` | INT | não | sim | não |
| `flgFrmCatAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `prcAlta` | SMALLINT | não | não | não |
| `prcMedia` | SMALLINT | não | não | não |
| `prcBaixa` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.FormCategoria` (idCat) → `dbo.Categoria` (idCat)
- `dbo.FormCategoria` (idFrm) → `dbo.Formulario` (idFrm)
