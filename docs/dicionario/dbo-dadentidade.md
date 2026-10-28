---
gerado: sincronizacao
---

# dbo.DadEntidade

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEnt` | INT | não | sim | não |
| `dsEntidade` | VARCHAR(50) | não | não | não |

## Chaves estrangeiras

- `dbo.DadContextoCampo` (idEnt) → `dbo.DadEntidade` (idEnt)
