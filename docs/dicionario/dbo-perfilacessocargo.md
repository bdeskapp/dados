---
gerado: sincronizacao
---

# dbo.PerfilAcessoCargo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPerCargo` | INT | não | sim | não |
| `idDom` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.PerfilAcessoCargo` (idDom) → `dbo.DadDominio` (idDom)
