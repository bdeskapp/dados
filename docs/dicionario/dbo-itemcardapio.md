---
gerado: sincronizacao
---

# dbo.ItemCardapio

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Nome` | NVARCHAR(255) | não | não | não |
| `Acao` | BIGINT | sim | não | não |
| `Slug` | NVARCHAR(255) | sim | não | não |
| `Categoria_ItemCardapio_id` | BIGINT | sim | não | não |
| `GruposAcesso` | NVARCHAR(255) | não | não | não |
| `MetaDados` | XML | não | não | não |
| `Padrao` | BIT | sim | não | não |
| `Categorizacao` | NVARCHAR(255) | sim | não | não |
| `Ativo` | BIT | não | não | não |
| `idFrm` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.GrupoAcesso_ItemCardapio` (idIc) → `dbo.ItemCardapio` (Id)
- `dbo.ItemCardapio` (Categoria_ItemCardapio_id) → `dbo.Categoria_ItemCardapio` (Id)
- `dbo.ItemCardapio` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.ReqConcluida` (idItemCardapio) → `dbo.ItemCardapio` (Id)
- `dbo.Requisicao` (ItemCardapio_id) → `dbo.ItemCardapio` (Id)
- `dbo.Req` (idItemCardapio) → `dbo.ItemCardapio` (Id)
