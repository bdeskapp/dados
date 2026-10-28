---
gerado: sincronizacao
---

# dbo.DocusignReq

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDocusignReq` | INT | não | sim | não |
| `idReq` | INT | não | não | não |
| `envelopeId` | VARCHAR(255) | sim | não | não |
| `dtUltimoAcesso` | DATETIME | sim | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `status` | VARCHAR(50) | sim | não | não |
| `idUsu` | INT | sim | não | não |
| `dadosCriacaoEnvelope` | VARCHAR(MAX) | sim | não | não |
| `accountId` | VARCHAR(255) | sim | não | não |

## Chaves estrangeiras

- `dbo.DocusignReq` (idUsu) → `dbo.Usuario` (idUsu)
