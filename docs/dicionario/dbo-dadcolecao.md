---
gerado: sincronizacao
---

# dbo.DadColecao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCon` | INT | não | sim | não |
| `idDad` | INT | não | sim | não |
| `nOrdem` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.DadColecao` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadColecao` (idDad) → `dbo.DadoAdicional` (idDad)
