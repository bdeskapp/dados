---
gerado: sincronizacao
---

# dbo.RotinaTransicao

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [workflow (processo e fluxo)](../fora-de-escopo/workflow.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotTran` | INT | não | sim | não |
| `idRotina` | INT | não | não | não |
| `idFrmTrans` | INT | não | não | não |
| `dsAlerta` | VARCHAR(200) | não | não | não |

## Chaves estrangeiras

- `dbo.RotinaTransicao` (idFrmTrans) → `dbo.FormTransicao` (idFrmTrans)
- `dbo.RotinaTransicao` (idRotina) → `dbo.Rotina` (idRotina)
- `dbo.TransicaoCondicional` (idRotTran) → `dbo.RotinaTransicao` (idRotTran)
