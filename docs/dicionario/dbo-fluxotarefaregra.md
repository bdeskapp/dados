---
gerado: sincronizacao
---

# dbo.FluxoTarefaRegra

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFlu` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |
| `idTarRef` | INT | não | sim | não |
| `flgDtIniObrig` | BIT | não | não | não |
| `flgDtFimObrig` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FluxoTarefaRegra` (idFlu, idTar) → `dbo.FluxoTarefa` (idFlu, idTar)
- `dbo.FluxoTarefaRegra` (idFlu, idTarRef) → `dbo.FluxoTarefa` (idFlu, idTar)
