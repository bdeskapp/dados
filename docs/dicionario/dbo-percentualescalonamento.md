---
gerado: sincronizacao
---

# dbo.PercentualEscalonamento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPrcEsc` | INT | não | sim | não |
| `nPrcEsc` | SMALLINT | não | não | não |
| `idUsu` | INT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.PercentualEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TipoEscalonamentoPercentual` (idPrcEsc) → `dbo.PercentualEscalonamento` (idPrcEsc)
- `dbo.UsuarioGrupoPrcEscalonamento` (idPrcEsc) → `dbo.PercentualEscalonamento` (idPrcEsc)
