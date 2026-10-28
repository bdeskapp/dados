---
gerado: sincronizacao
---

# dbo.PesqOpcConjunto

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idOpcConj` | INT | não | sim | não |
| `dsOpcConj` | VARCHAR(200) | não | não | não |
| `idGru` | INT | não | não | não |
| `flgOpcConjAtivo` | BIT | não | não | não |
| `tpFormato` | CHAR(1) | sim | não | não |

## Chaves estrangeiras

- `dbo.PesqOpcao` (idOpcConj) → `dbo.PesqOpcConjunto` (idOpcConj)
- `dbo.PesqPergunta` (idOpcConj) → `dbo.PesqOpcConjunto` (idOpcConj)
