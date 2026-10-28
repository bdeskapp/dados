---
gerado: sincronizacao
---

# dbo.TipoLigacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpli` | INT | não | sim | não |
| `dsTpli` | VARCHAR(30) | não | não | não |
| `flgTpliAtivo` | BIT | não | não | não |
| `idAre` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.RegistroLigacao` (idTpli) → `dbo.TipoLigacao` (idTpli)
