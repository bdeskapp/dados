---
gerado: sincronizacao
---

# dbo.DadDominioLog

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDom` | INT | não | não | não |
| `idDad` | INT | não | não | não |
| `dsDom` | VARCHAR(150) | sim | não | não |
| `dsLegenda` | VARCHAR(500) | sim | não | não |
| `idDomPai` | INT | sim | não | não |
| `idUsu` | INT | não | não | não |
| `tpOper` | CHAR(1) | não | não | não |
| `dtLog` | DATETIME | não | não | não |
| `tpForma` | CHAR(1) | não | não | não |
| `atributos` | VARCHAR(MAX) | sim | não | não |
