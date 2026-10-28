---
gerado: sincronizacao
---

# dbo.DadFormAcao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idFrmAcao` | INT | não | sim | não |
| `flgObrigatorio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadFormAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadFormAcao` (idFrmAcao) → `dbo.FormAcao` (idFrmAcao)
