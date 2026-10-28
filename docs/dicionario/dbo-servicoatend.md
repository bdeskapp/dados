---
gerado: sincronizacao
---

# dbo.ServicoAtend

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAre` | INT | não | sim | não |
| `dsServico` | VARCHAR(50) | não | não | não |
| `idGruAcesso` | INT | não | não | não |
| `idGruAtend` | INT | não | não | não |
| `idFrm` | INT | não | não | não |
| `dsAssinatura` | VARCHAR(250) | sim | não | não |
| `idObj` | INT | não | não | não |
| `idObjReg` | INT | sim | não | não |
| `idObjLig` | INT | sim | não | não |
| `idObjAco` | INT | sim | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idObjAR` | INT | sim | não | não |
| `idFrmNC` | INT | sim | não | não |
| `idProcNC` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.ServicoAtend` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.ServicoAtend` (idGruAtend) → `dbo.Grupo` (idGru)
- `dbo.ServicoAtend` (idGruAcesso) → `dbo.GrupoAcesso` (idGru)
