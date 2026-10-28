---
gerado: sincronizacao
---

# dbo.SubCategoria

**Selo:** Explicada

Explicada em:

- [classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idSca` | INT | não | sim | não |
| `dsSca` | VARCHAR(100) | sim | não | não |
| `idCat` | INT | não | não | não |
| `flgScaAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idMascara` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadContextoCampo` (idSca) → `dbo.SubCategoria` (idSca)
- `dbo.SubCategoriaAcesso` (idSca) → `dbo.SubCategoria` (idSca)
- `dbo.SubCategoria` (idCat) → `dbo.Categoria` (idCat)
- `dbo.SubCategoria` (idMascara) → `dbo.Mascara` (idMascara)
- `dbo.Tarefa` (idSca) → `dbo.SubCategoria` (idSca)
