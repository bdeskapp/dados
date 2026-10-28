---
gerado: sincronizacao
---

# dbo.UsuarioCampoLayout

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `idCampoL` | INT | não | sim | não |
| `usuOrdemL` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.UsuarioCampoLayout` (idCampoL) → `dbo.CampoLayout` (idCampoL)
- `dbo.UsuarioCampoLayout` (idUsu) → `dbo.Usuario` (idUsu)
