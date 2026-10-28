---
gerado: sincronizacao
---

# dbo.FormPapelPatDom

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatDom` | INT | não | sim | não |
| `idFrmPapel` | INT | não | não | não |
| `idClas` | INT | não | não | não |
| `idTpp` | INT | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPapelPatDom` (idClas) → `dbo.Classe` (idClas)
- `dbo.FormPapelPatDom` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelPatDom` (idTpp) → `dbo.TipoPatrimonio` (idTpp)
