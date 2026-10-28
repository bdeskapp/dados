---
gerado: sincronizacao
---

# dbo.TipoTarefa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idTpTa` | INT | não | sim | não |
| `dsTpTa` | VARCHAR(30) | não | não | não |
| `flgTpTaAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FormPesqCriterio` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
- `dbo.FormTipoTarefa` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
- `dbo.TipoEscalonamento` (idTpTa) → `dbo.TipoTarefa` (idTpTa)
