---
gerado: sincronizacao
---

# dbo.DadRelacionamento

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idDadConRel` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadRelacionamento` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadRelacionamento` (idDadConRel) → `dbo.DadContextoCampo` (idDadCon)
