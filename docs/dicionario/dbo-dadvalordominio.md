---
gerado: sincronizacao
---

# dbo.DadValorDominio

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadVal` | INT | não | sim | não |
| `idDom` | INT | não | sim | não |

## Chaves estrangeiras

- `dbo.DadValorDominio` (idDom) → `dbo.DadDominio` (idDom)
- `dbo.DadValorDominio` (idDadVal) → `dbo.DadValor` (idDadVal)
