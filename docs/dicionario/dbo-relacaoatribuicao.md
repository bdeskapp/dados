---
gerado: sincronizacao
---

# dbo.RelacaoAtribuicao

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelEfeito` | INT | não | sim | não |
| `idRotinaDestino` | INT | não | não | não |
| `idDadConDestino` | INT | não | não | não |
| `numero` | DECIMAL(15,4) | sim | não | não |
| `string` | VARCHAR(1000) | sim | não | não |
| `data` | DATETIME | sim | não | não |
| `boolean` | BIT | sim | não | não |
| `dinheiro` | MONEY | sim | não | não |
| `flgDataAtual` | BIT | sim | não | não |
| `idRotinaOrigem` | INT | sim | não | não |
| `idDadConOrigem` | INT | sim | não | não |
| `flgIncrementar` | BIT | sim | não | não |
| `flgDecrementar` | BIT | sim | não | não |
| `flgNull` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.RelacaoAtribuicaoDom` (idRelEfeito) → `dbo.RelacaoAtribuicao` (idRelEfeito)
- `dbo.RelacaoAtribuicaoTab` (idRelEfeito) → `dbo.RelacaoAtribuicao` (idRelEfeito)
- `dbo.RelacaoAtribuicao` (idDadConOrigem) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.RelacaoAtribuicao` (idDadConDestino) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.RelacaoAtribuicao` (idRelEfeito) → `dbo.RelacaoEfeito` (idRelEfeito)
- `dbo.RelacaoAtribuicao` (idRotinaOrigem) → `dbo.Rotina` (idRotina)
- `dbo.RelacaoAtribuicao` (idRotinaDestino) → `dbo.Rotina` (idRotina)
