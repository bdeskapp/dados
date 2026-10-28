---
gerado: sincronizacao
---

# dbo.DadProcesso

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRotina` | INT | não | sim | não |
| `idDadCon` | INT | não | sim | não |
| `flgInicio` | BIT | não | não | não |
| `flgConc` | BIT | não | não | não |
| `flgCanc` | BIT | não | não | não |
| `flgAberta` | BIT | não | não | não |
| `flgEncerrada` | BIT | não | não | não |
| `flgEdit1` | BIT | não | não | não |
| `flgEdit2` | BIT | não | não | não |
| `flgEdit3` | BIT | não | não | não |
| `flgEdit4` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadProcesso` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadProcesso` (idRotina) → `dbo.Rotina` (idRotina)
