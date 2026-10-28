---
gerado: sincronizacao
---

# dbo.CondDad

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCond` | INT | não | sim | não |
| `idDadCon` | INT | não | não | não |
| `tpOperador` | CHAR(6) | não | não | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `flgDataAtual` | BIT | sim | não | não |

## Chaves estrangeiras

- `dbo.CondDadDominio` (idCond) → `dbo.CondDad` (idCond)
- `dbo.CondDadTabela` (idCond) → `dbo.CondDad` (idCond)
- `dbo.CondDad` (idCond) → `dbo.Condicao` (idCond)
- `dbo.CondDad` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
