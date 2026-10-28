---
gerado: sincronizacao
---

# dbo.DadDefault

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |

## Chaves estrangeiras

- `dbo.DadDefault` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
