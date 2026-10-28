---
gerado: sincronizacao
---

# dbo.ReqKB

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

- `dbo.ReqKB` (idGru) → `dbo.Grupo` (idGru)
- `dbo.ReqKB` (idKB) → `dbo.KBase` (idKB)
- `dbo.ReqKB` (idReq) → `dbo.Req` (idReq)
- `dbo.ReqKB` (idReqPart) → `dbo.ReqParticipante` (idReqPart)
- `dbo.ReqKB` (idUsu) → `dbo.Usuario` (idUsu)
