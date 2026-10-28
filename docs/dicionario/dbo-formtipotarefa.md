---
gerado: sincronizacao
---

# dbo.FormTipoTarefa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrm` | INT | não | sim | não |
| `idTpTa` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormTipoTarefa` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.FormTipoTarefa` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
