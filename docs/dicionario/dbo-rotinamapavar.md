---
gerado: sincronizacao
---

# dbo.RotinaMapaVar

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotinaOrigem` | INT | não | sim | não |
| `idRotinaDestino` | INT | não | sim | não |
| `tpCopiaAssunto` | TINYINT | não | não | não |
| `tpCopiaDescricao` | TINYINT | não | não | não |
| `tpCopiaVerba` | TINYINT | não | não | não |
| `tpCopiaLocalizacao` | TINYINT | não | não | não |
| `tpCopiaPrioridade` | TINYINT | não | não | não |
| `tpCopiaOrigem` | TINYINT | não | não | não |
| `idAcaoCopiaDescricao` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RotinaMapaVar` (idAcaoCopiaDescricao) → `dbo.Acao` (idAcao)
- `dbo.RotinaMapaVar` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaVar` (idRotinaDestino) → `dbo.Rotina` (idRotina)
