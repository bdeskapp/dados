---
gerado: sincronizacao
---

# dbo.AplicacaoExterna

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idApp` | INT | não | sim | não |
| `nmApp` | VARCHAR(100) | não | não | não |
| `flgAtivo` | BIT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `dtInclusao` | DATETIME | não | não | não |
| `dtExclusao` | DATETIME | sim | não | não |
| `idUsuAtualizacao` | INT | sim | não | não |
| `dtAtualizacao` | DATETIME | sim | não | não |
| `idTpApp` | INT | sim | não | não |
| `urlWebService` | VARCHAR(200) | sim | não | não |
| `idAppCliente` | VARCHAR(20) | sim | não | não |
| `returnUrl` | VARCHAR(200) | sim | não | não |

## Chaves estrangeiras

- `dbo.AplicacaoExterna` (idUsuAtualizacao) → `dbo.Usuario` (idUsu)
