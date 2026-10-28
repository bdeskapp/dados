---
gerado: sincronizacao
---

# dbo.KBRotina

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idKb` | INT | não | sim | não |
| `idFrm` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.KBRotina` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.KBRotina` (idKb) → `dbo.KBase` (idKB)
