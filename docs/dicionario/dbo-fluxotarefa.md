---
gerado: sincronizacao
---

# dbo.FluxoTarefa

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlu` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |
| `dependencia` | VARCHAR(70) | sim | não | não |
| `flgCriticidade` | TINYINT | não | não | não |
| `sqOrdem` | INT | sim | não | não |
| `idAre` | INT | não | não | não |
| `idFluTar` | INT | não | não | não |
| `DependenciaAntiga` | VARCHAR(70) | sim | não | não |

## Chaves estrangeiras

- `dbo.FluxoTarefaRegra` (idFlu, idTar) → `dbo.FluxoTarefa` (idFlu, idTar)
- `dbo.FluxoTarefaRegra` (idFlu, idTarRef) → `dbo.FluxoTarefa` (idFlu, idTar)
- `dbo.FluxoTarefa` (idAre) → `dbo.Area` (idAre)
- `dbo.FluxoTarefa` (idFlu) → `dbo.Fluxo` (idFlu)
- `dbo.FluxoTarefa` (idTar) → `dbo.Tarefa` (idTar)
