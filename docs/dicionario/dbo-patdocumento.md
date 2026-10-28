---
gerado: sincronizacao
---

# dbo.PatDocumento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDoc` | INT | não | sim | não |
| `idDocOriginal` | INT | sim | não | não |
| `nVersao` | TINYINT | não | não | não |
| `idPat` | INT | sim | não | não |
| `nmDocFisico` | VARCHAR(155) | não | não | não |
| `dsTitulo` | VARCHAR(255) | não | não | não |
| `idOwner` | INT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `dtInvalidacao` | DATETIME | sim | não | não |
| `flgInvalido` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.PatDocumento` (idDocOriginal) → `dbo.PatDocumento` (idDoc)
- `dbo.PatDocumento` (idPat) → `dbo.Patrimonio` (idPat)
- `dbo.PatDocumento` (idOwner) → `dbo.Usuario` (idUsu)
