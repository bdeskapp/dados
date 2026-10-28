---
gerado: sincronizacao
---

# dbo.ReqKBConcluida

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [base de conhecimento](../fora-de-escopo/base-de-conhecimento.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReq` | INT | não | sim | não |
| `idKB` | INT | não | sim | não |
| `dtKB` | DATETIME | não | não | não |
| `idUsu` | INT | não | não | não |
| `idGru` | INT | sim | não | não |
| `idReqPart` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.ReqKBConcluida` (idKB) → `dbo.KBase` (idKB)
- `dbo.ReqKBConcluida` (idReq) → `dbo.ReqConcluida` (idReq)
