---
gerado: sincronizacao
---

# dbo.FluxoOsAnexo

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idAne` | INT | não | sim | não |
| `idFlo` | INT | não | não | não |
| `Anexo` | VARCHAR(155) | não | não | não |
| `Titulo` | VARCHAR(255) | não | não | não |
| `dtInclusao` | SMALLDATETIME | não | não | não |
| `idUsuResponsavel` | INT | não | não | não |
| `flgInvalido` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FluxoOsAnexoGrupo` (idAne) → `dbo.FluxoOsAnexo` (idAne)
- `dbo.FluxoOsAnexo` (idFlo) → `dbo.FluxoOS` (idFlO)
