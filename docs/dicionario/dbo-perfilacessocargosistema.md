---
gerado: sincronizacao
---

# dbo.PerfilAcessoCargoSistema

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idPerCargo` | INT | não | sim | não |
| `idDad` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.PerfilAcessoCargoSistema` (idDad) → `dbo.DadoAdicional` (idDad)
