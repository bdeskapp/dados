---
gerado: sincronizacao
---

# dbo.Efeito

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idCausa` | INT | não | sim | não |
| `idRelEfeito` | INT | não | sim | não |
| `nSeq` | SMALLINT | não | sim | não |
| `dtExec` | DATETIME | sim | não | não |
| `status` | CHAR(1) | não | não | não |
| `dsLog` | TEXT | sim | não | não |
| `idRotinaEfeito` | INT | sim | não | não |
| `idReqPart` | INT | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `flgAbertura` | BIT | não | não | não |
| `dtRegistro` | DATETIME | não | não | não |

## Chaves estrangeiras

- `dbo.Efeito` (idCausa) → `dbo.Causa` (idCausa)
- `dbo.Efeito` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.Efeito` (idRotinaEfeito) → `dbo.Rotina` (idRotina)
- `dbo.Efeito` (idUsu) → `dbo.Usuario` (idUsu)
