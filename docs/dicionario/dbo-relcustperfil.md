---
gerado: sincronizacao
---

# dbo.RelCustPerfil

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelCust` | INT | não | sim | não |
| `idPer` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.RelCustPerfil` (idPer) → `dbo.Perfil` (idPer)
- `dbo.RelCustPerfil` (idRelCust) → `dbo.RelCust` (idRelCust)
