---
gerado: sincronizacao
---

# dbo.FormPapelObrigatorioTarefa

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFrmPapel` | INT | não | sim | não |
| `idTar` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.FormPapelObrigatorioTarefa` (idFrmPapel) → `dbo.FormPapel` (idFrmPapel)
- `dbo.FormPapelObrigatorioTarefa` (idTar) → `dbo.Tarefa` (idTar)
