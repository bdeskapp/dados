---
gerado: sincronizacao
---

# dbo.RotinaMapaPapel

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotinaOrigem` | INT | não | sim | não |
| `idFrmPapelOrigem` | INT | não | sim | não |
| `idRotinaDestino` | INT | não | sim | não |
| `idFrmPapelDestino` | INT | não | sim | não |
| `flgObrigatorio` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.RotinaMapaPapel` (idFrmPapelOrigem) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RotinaMapaPapel` (idFrmPapelDestino) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RotinaMapaPapel` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RotinaMapaPapel` (idRotinaDestino) → `dbo.Rotina` (idRotina)
