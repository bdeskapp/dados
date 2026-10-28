---
gerado: sincronizacao
---

# dbo.OsAnexoConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAnexo` | INT | não | sim | não |
| `idOS` | INT | não | sim | não |
| `anexo` | VARCHAR(155) | não | não | não |
| `Titulo` | VARCHAR(255) | não | não | não |
| `dtInclusao` | SMALLDATETIME | não | não | não |
| `idUsuResponsavel` | INT | não | não | não |
| `flgInvalido` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.OsAnexoConcluida` (idOS) → `dbo.OSConcluida` (idOs)
- `dbo.OsAnexoConcluida` (idUsuResponsavel) → `dbo.Usuario` (idUsu)
