---
gerado: sincronizacao
---

# dbo.FormPapelObrigatorioDadoAdicional

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `idDadCon` | INT | não | sim | não |
| `tpOper` | VARCHAR(7) | sim | não | não |
| `tpPreenchido` | TINYINT | sim | não | não |
| `tpBoolean` | TINYINT | sim | não | não |
| `valNumerico1` | DECIMAL(15,4) | sim | não | não |
| `valNumerico2` | DECIMAL(15,4) | sim | não | não |
| `valDominio` | VARCHAR(500) | sim | não | não |

## Chaves estrangeiras

- `dbo.FormPapelObrigatorioDadoAdicional` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.FormPapelObrigatorioDadoAdicional` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
