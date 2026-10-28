---
gerado: sincronizacao
---

# dbo.DadContextoVinc

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idFrmRel` | INT | não | não | não |
| `tpReq` | CHAR(1) | sim | não | não |
| `flgMult` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoVinc` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
