---
gerado: sincronizacao
---

# dbo.DadoAdicionalUsuarioLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDad` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `dtInclusao` | DATETIME | não | sim | não |
| `idUsuInclusao` | INT | não | não | não |
| `tpOperacao` | CHAR(1) | não | não | não |

## Chaves estrangeiras

- `dbo.DadoAdicionalUsuarioLog` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicionalUsuarioLog` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.DadoAdicionalUsuarioLog` (idUsuInclusao) → `dbo.Usuario` (idUsu)
