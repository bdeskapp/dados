---
gerado: sincronizacao
---

# dbo.Idioma

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdIdioma` | CHAR(5) | não | sim | não |
| `dsIdioma` | VARCHAR(20) | não | não | não |
| `dsIcone` | VARCHAR(20) | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `owner` | VARCHAR(10) | não | não | não |

## Chaves estrangeiras

- `dbo.Usuario` (cdIdioma) → `dbo.Idioma` (cdIdioma)
