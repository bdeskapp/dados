---
gerado: sincronizacao
---
# Receita: volume de requisições por canal de abertura


## 1. Pergunta e indicador

- **Pergunta:** quantas requisições foram abertas por cada canal (automática, e-mail, abertura pelas telas de atendimento ou por desdobramento, processo (fluxo), agenda recorrente, abertura pela tela de pedido do portal web ou pela API), somando as abertas e as encerradas?
- **Indicador:** volume do canal = número de requisições (abertas + encerradas) cuja data de abertura (`dtAbertura`) cai no período, agrupadas por `tpAgenteReg`.

## 2. Definição usada

- Canal = `tpAgenteReg`, gravado na abertura, com os códigos e rótulos de [Valores definidos pelo produto](../dominios-do-produto.md) (decisão do produto): `A` automática, `E` e-mail, `M` abertura pelas telas de atendimento ou por desdobramento, `P` processo (fluxo), `R` agenda recorrente, `X` abertura pela tela de pedido do portal web ou pela API.
- A coluna admite `NULL` (abertura sem código); essas requisições formam uma linha com `canal` vazio.
- A origem do contato (`idFrmOrigem → FormOrigem`) é outra coluna e não entra nesta receita ([Canal e origem](../dimensoes/canal-origem.md)).
- O período é o de `dtAbertura`, preenchida nas duas tabelas; o estado atual não entra no filtro. Volume = abertas + encerradas ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O primeiro ramo é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente.

```sql
SELECT x.canal,
       SUM(x.qtd) AS qtd_requisicoes
FROM (
    SELECT r.tpAgenteReg AS canal, COUNT(*) AS qtd
    FROM Req r WITH(NOLOCK)
    WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
    GROUP BY r.tpAgenteReg
    UNION ALL
    SELECT c.tpAgenteReg, COUNT(*)
    FROM ReqConcluida c WITH(NOLOCK)
    WHERE c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
    GROUP BY c.tpAgenteReg
) x
GROUP BY x.canal
ORDER BY x.canal;
```

Granularidade do resultado: uma linha por canal (incluindo a linha do canal vazio).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | canal | qtd_requisicoes |
    |---|---|
    | | 5 |
    | E | 300 |
    | M | 900 |

## 5. Regras aplicadas

- [R-canal-origem-01](../dimensoes/canal-origem.md): leia o canal de abertura em `tpAgenteReg` e some abertas e encerradas.
- [R-canal-origem-03](../dimensoes/canal-origem.md): trate o canal vazio como parte do resultado.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas para qualquer volume histórico.

## Veja também

- [Dimensão: canal e origem](../dimensoes/canal-origem.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Receita: volume por mês](volume-por-mes.md)
