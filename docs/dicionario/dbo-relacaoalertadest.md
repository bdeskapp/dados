---
gerado: sincronizacao
---

# dbo.RelacaoAlertaDest

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | não | não |
| `idRotina` | INT | sim | não | não |
| `idFrmPapel` | INT | sim | não | não |
| `idTpPapel` | SMALLINT | sim | não | não |
| `idPart` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.RelacaoAlertaDest` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.RelacaoAlertaDest` (idTpPapel, idPart) → `dbo.PartTipoPapel` (idTpPapel, idPart)
- `dbo.RelacaoAlertaDest` (idRelEfeito) → `dbo.RelacaoAlerta` (idRelEfeito)
- `dbo.RelacaoAlertaDest` (idRotina) → `dbo.Rotina` (idRotina)
