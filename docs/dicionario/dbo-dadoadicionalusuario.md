---
gerado: sincronizacao
---

# dbo.DadoAdicionalUsuario

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDad` | INT | não | sim | não |
| `idUsu` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadoAdicionalUsuario` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadoAdicionalUsuario` (idUsu) → `dbo.Usuario` (idUsu)
