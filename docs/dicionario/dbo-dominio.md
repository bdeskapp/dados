---
gerado: sincronizacao
---

# dbo.Dominio

**Selo:** Explicada

Explicada em:

- [pessoa e organização](../dimensoes/pessoa-organizacao.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDom` | INT | não | sim | não |
| `nmDom` | VARCHAR(30) | não | não | não |
| `flgDomAtivo` | BIT | não | não | não |
| `IdConexaoLDAP` | INT | sim | não | não |
| `flgDefault` | BIT | não | não | não |
| `urlLDAPRemoto` | VARCHAR(200) | sim | não | não |

## Chaves estrangeiras

- `dbo.SyncUsuConfig` (idDom) → `dbo.Dominio` (idDom)
- `dbo.Usuario` (idDom) → `dbo.Dominio` (idDom)
