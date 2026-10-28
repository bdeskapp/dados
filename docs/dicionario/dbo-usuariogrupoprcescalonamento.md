---
gerado: sincronizacao
---

# dbo.UsuarioGrupoPrcEscalonamento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idGru` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |
| `idPrcEsc` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.UsuarioGrupoPrcEscalonamento` (idGru) → `dbo.Grupo` (idGru)
- `dbo.UsuarioGrupoPrcEscalonamento` (idPrcEsc) → `dbo.PercentualEscalonamento` (idPrcEsc)
- `dbo.UsuarioGrupoPrcEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
