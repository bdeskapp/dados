---
gerado: sincronizacao
---

# dbo.MonitorConfig

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUsu` | INT | não | sim | não |
| `IntervaloVerificacao` | SMALLINT | não | não | não |
| `flgMonitoracaoAtivada` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.MonitorConfig` (idUsu) → `dbo.Usuario` (idUsu)
