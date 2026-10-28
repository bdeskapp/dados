---
gerado: sincronizacao
---

# dbo.DadAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idAcao` | INT | não | sim | não |
| `flgObrigatorio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadAcao` (idAcao) → `dbo.Acao` (idAcao)
- `dbo.DadAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
