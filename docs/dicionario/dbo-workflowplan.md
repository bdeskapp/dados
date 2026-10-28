---
gerado: sincronizacao
---

# dbo.WorkflowPlan

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlu` | INT | não | sim | não |
| `idRotina` | INT | não | sim | não |
| `dtPlan` | DATETIME | não | sim | não |
| `idUsu` | INT | não | não | não |
| `dtIniPrev` | DATETIME | sim | não | não |
| `dtFimPrev` | DATETIME | sim | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |
| `idPart` | INT | sim | não | não |
| `dtIniReal` | DATETIME | sim | não | não |
| `dtFimReal` | DATETIME | sim | não | não |
| `idReq` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.WorkflowPlan` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.WorkflowPlan` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.WorkflowPlan` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.WorkflowPlan` (idFlu) → `dbo.Workflow` (idFlu)
