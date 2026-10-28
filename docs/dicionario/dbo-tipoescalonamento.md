---
gerado: sincronizacao
---

# dbo.TipoEscalonamento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpEsc` | INT | não | sim | não |
| `nmTpEsc` | VARCHAR(200) | não | não | não |
| `nPrcEsc` | VARCHAR(200) | sim | não | não |
| `nPrioridade` | TINYINT | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `nImp` | TINYINT | sim | não | não |
| `nUrg` | TINYINT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `idTpTa` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.TipoEscalonamentoPercentual` (idTpEsc) → `dbo.TipoEscalonamento` (idTpEsc)
- `dbo.TipoEscalonamento` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.TipoEscalonamento` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
- `dbo.UsuarioGrupo` (idTpEsc) → `dbo.TipoEscalonamento` (idTpEsc)
