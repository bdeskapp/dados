---
gerado: sincronizacao
---

# dbo.CRM_ContratoDoc

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDoc` | INT | não | sim | não |
| `idDocOriginal` | INT | sim | não | não |
| `nVersao` | TINYINT | não | não | não |
| `idContrato` | INT | sim | não | não |
| `nmDocFisico` | VARCHAR(155) | não | não | não |
| `dsTitulo` | VARCHAR(255) | não | não | não |
| `idOwner` | INT | não | não | não |
| `dtInclusao` | SMALLDATETIME | não | não | não |
| `dtInvalidacao` | SMALLDATETIME | sim | não | não |
| `flgInvalido` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_ContratoDoc` (idContrato) → `dbo.CRM_Contrato` (idContrato)
- `dbo.CRM_ContratoDoc` (idDocOriginal) → `dbo.CRM_ContratoDoc` (idDoc)
- `dbo.CRM_ContratoDoc` (idOwner) → `dbo.Usuario` (idUsu)
