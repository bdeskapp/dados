---
gerado: sincronizacao
---

# dbo.RelacaoAlerta

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idFrmNotMsg` | INT | sim | não | não |
| `dsTitulo` | VARCHAR(500) | sim | não | não |
| `dsMensagem` | VARCHAR(4000) | sim | não | não |

## Chaves estrangeiras

- `dbo.RelacaoAlertaDest` (idRelEfeito) → `dbo.RelacaoAlerta` (idRelEfeito)
- `dbo.RelacaoAlerta` (idFrmNotMsg) → `dbo.FormNotMensagem` (idFrmNotMsg)
- `dbo.RelacaoAlerta` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
