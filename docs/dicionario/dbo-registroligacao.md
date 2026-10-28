---
gerado: sincronizacao
---

# dbo.RegistroLigacao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | não | não |
| `idAtendente` | INT | não | não | não |
| `dtIniRlig` | DATETIME | não | não | não |
| `dtFimRlig` | DATETIME | não | não | não |
| `idTpli` | INT | não | não | não |
| `idHie` | INT | sim | não | não |
| `idAre` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.RegistroLigacao` (idHie) → `dbo.OrgHierarquia` (idHie)
- `dbo.RegistroLigacao` (idUsu) → `dbo.Usuario` (idUsu)
- `dbo.RegistroLigacao` (idAtendente) → `dbo.Usuario` (idUsu)
- `dbo.RegistroLigacao` (idTpli) → `dbo.TipoLigacao` (idTpli)
