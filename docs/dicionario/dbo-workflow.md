---
gerado: sincronizacao
---

# dbo.Workflow

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlu` | INT | não | sim | não |
| `idProc` | INT | sim | não | não |
| `dsTitulo` | VARCHAR(300) | sim | não | não |
| `dtInicio` | DATETIME | não | não | não |
| `dtFim` | DATETIME | sim | não | não |
| `idRotinaAtual` | INT | sim | não | não |
| `qtdAberta` | TINYINT | não | não | não |
| `qtdPendente` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.Causa` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqConcluida` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqConcluida` (idFluPai) → `dbo.Workflow` (idFlu)
- `dbo.ReqDocConcluida` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqDocumento` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.ReqVinculada` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.Req` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.Req` (idFluPai) → `dbo.Workflow` (idFlu)
- `dbo.WorkflowPlan` (idFlu) → `dbo.Workflow` (idFlu)
- `dbo.Workflow` (idProc) → `dbo.Processo` (idProc)
- `dbo.Workflow` (idRotinaAtual) → `dbo.Rotina` (idRotina)
