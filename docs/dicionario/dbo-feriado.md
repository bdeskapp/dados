---
gerado: sincronizacao
---

# dbo.Feriado

**Selo:** Explicada

Explicada em:

- [calendário de atendimento](../dimensoes/tempo-calendario.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFer` | INT | não | sim | não |
| `dsFer` | VARCHAR(50) | não | não | não |
| `dia` | CHAR(2) | sim | não | não |
| `mes` | CHAR(2) | sim | não | não |
| `flgMovel` | BIT | não | não | não |
| `idUsuOperacao` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.Feriado` (idUsuOperacao) → `dbo.Usuario` (idUsu)
