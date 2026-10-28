---
gerado: sincronizacao
---

# dbo.DadContextoCampoEditabilidade

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `flgSolicita` | BIT | não | não | não |
| `flgAtende` | BIT | não | não | não |
| `flgAcompanha` | BIT | não | não | não |
| `flgAdministra` | BIT | não | não | não |
| `flgOcultarAbertura` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoCampoEditabilidade` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
