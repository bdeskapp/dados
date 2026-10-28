---
gerado: sincronizacao
---

# dbo.TipoEscalonamentoPercentual

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpEsc` | INT | não | não | não |
| `idPrcEsc` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.TipoEscalonamentoPercentual` (idPrcEsc) → `dbo.PercentualEscalonamento` (idPrcEsc)
- `dbo.TipoEscalonamentoPercentual` (idTpEsc) → `dbo.TipoEscalonamento` (idTpEsc)
- `dbo.TipoEscalonamentoPercentual` (idUsu) → `dbo.Usuario` (idUsu)
