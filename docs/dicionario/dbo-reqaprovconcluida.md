---
gerado: sincronizacao
---

# dbo.ReqAprovConcluida

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idReqAprov` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `idTpPapel` | SMALLINT | não | não | não |
| `idPart` | INT | não | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `flgConvocado` | BIT | não | não | não |
| `flgSubstituido` | BIT | não | não | não |
| `tpResultado` | CHAR(1) | sim | não | não |
