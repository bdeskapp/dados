---
gerado: sincronizacao
---

# dbo.Marca

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMar` | INT | não | sim | não |
| `dsMar` | VARCHAR(60) | não | não | não |
| `flgMarAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.KBPat` (idMar) → `dbo.Marca` (idMar)
- `dbo.MarcaTipoPat` (idMar) → `dbo.Marca` (idMar)
- `dbo.Patrimonio` (idMar) → `dbo.Marca` (idMar)
