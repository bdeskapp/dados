---
gerado: sincronizacao
---

# dbo.DadValor

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [Modelo: a requisição no centro](../mapa/modelo.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadVal` | INT | não | sim | não |
| `idQQ` | INT | não | não | não |
| `idDadCon` | INT | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `flgAgenda` | BIT | sim | não | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `texto` | TEXT | sim | não | não |
| `nSeq` | SMALLINT | não | não | não |

## Chaves estrangeiras

- `dbo.DadValorDominio` (idDadVal) → `dbo.DadValor` (idDadVal)
- `dbo.DadValorTabela` (idDadVal) → `dbo.DadValor` (idDadVal)
- `dbo.DadValor` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
