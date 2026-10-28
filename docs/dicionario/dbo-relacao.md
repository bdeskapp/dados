---
gerado: sincronizacao
---

# dbo.Relacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRel` | INT | não | sim | não |
| `idRotinaCausa` | INT | sim | não | não |
| `idRotinaEfeito` | INT | sim | não | não |
| `tpCausa` | CHAR(1) | não | não | não |
| `tpEfeito` | CHAR(10) | não | não | não |
| `dsRelacao` | VARCHAR(100) | não | não | não |
| `idFrmCausa` | INT | não | não | não |
| `idFrmEfeito` | INT | não | não | não |
| `nSeq` | SMALLINT | não | não | não |
| `idFrmAcaoOrigem` | INT | sim | não | não |
| `flgRepeat` | BIT | não | não | não |
| `tpRelacao` | CHAR(1) | não | não | não |
| `stpRelacao` | CHAR(1) | não | não | não |
| `flgExecutaProcEncerrado` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.Causa` (idRel) → `dbo.Relacao` (idRel)
- `dbo.RelacaoCondicao` (idRel) → `dbo.Relacao` (idRel)
- `dbo.RelacaoEfeito` (idRel) → `dbo.Relacao` (idRel)
- `dbo.RelacaoStatus` (idRel) → `dbo.Relacao` (idRel)
- `dbo.RelacaoTimeout` (idRel) → `dbo.Relacao` (idRel)
- `dbo.Relacao` (idFrmAcaoOrigem) → `dbo.FormAcao` (idFrmAcao)
- `dbo.Relacao` (idFrmCausa) → `dbo.Formulario` (idFrm)
- `dbo.Relacao` (idFrmEfeito) → `dbo.Formulario` (idFrm)
- `dbo.Relacao` (idRotinaCausa) → `dbo.Rotina` (idRotina)
- `dbo.Relacao` (idRotinaEfeito) → `dbo.Rotina` (idRotina)
