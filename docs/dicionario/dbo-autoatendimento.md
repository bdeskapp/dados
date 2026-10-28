---
gerado: sincronizacao
---

# dbo.AutoAtendimento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAut` | INT | não | sim | não |
| `dtIncAlt` | DATETIME | não | não | não |
| `idKb` | INT | não | não | não |
| `idUsu` | INT | sim | não | não |
| `Login` | VARCHAR(50) | sim | não | não |
| `dsKB` | TEXT | não | não | não |

## Chaves estrangeiras

- `dbo.AutoAtendimento` (idKb) → `dbo.KBase` (idKB)
- `dbo.AutoAtendimento` (idUsu) → `dbo.Usuario` (idUsu)
