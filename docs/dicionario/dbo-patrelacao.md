---
gerado: sincronizacao
---

# dbo.PatRelacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPatRel` | INT | não | sim | não |
| `dsPatRel` | VARCHAR(40) | não | não | não |
| `tpRel` | CHAR(1) | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `tpCriticidade` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.PatOperacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAssociadoSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAssociado` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAtributoSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.PatrimonioAtributo` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.UsuarioPatrimonioSolicitacao` (idPatRel) → `dbo.PatRelacao` (idPatRel)
- `dbo.UsuarioPatrimonio` (idPatRel) → `dbo.PatRelacao` (idPatRel)
