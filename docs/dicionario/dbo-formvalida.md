---
gerado: sincronizacao
---

# dbo.FormValida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | não | não |
| `idRegra` | INT | não | não | não |
| `tpErro` | CHAR(1) | não | não | não |
| `dsErro` | VARCHAR(500) | não | não | não |

## Chaves estrangeiras

- `dbo.FormValida` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormValida` (idRegra) → `dbo.Regra` (idRegra)
