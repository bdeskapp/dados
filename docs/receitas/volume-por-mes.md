---
gerado: sincronizacao
---
# Receita: volume de requisições por mês


## 1. Pergunta e indicador

- **Pergunta:** quantas requisições foram abertas em cada mês, somando as que ainda estão abertas e as já encerradas?
- **Indicador:** volume do mês = número de requisições (abertas + encerradas) cuja data de abertura (`dtAbertura`) cai naquele mês.

## 2. Definição usada

- O mês é o de `dtAbertura`, coluna sempre preenchida nas duas tabelas.
- Volume = abertas + encerradas: `Req` e `ReqConcluida` não têm `idReq` em comum ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).
- O estado atual da requisição não entra no filtro: uma requisição aberta em março e encerrada em maio conta em março.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O primeiro ramo é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente.

```sql
SELECT x.mes, SUM(x.qtd) AS qtd_requisicoes
FROM (
    SELECT DATEFROMPARTS(YEAR(r.dtAbertura), MONTH(r.dtAbertura), 1) AS mes, COUNT(*) AS qtd
    FROM Req r WITH(NOLOCK)
    WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
    GROUP BY DATEFROMPARTS(YEAR(r.dtAbertura), MONTH(r.dtAbertura), 1)
    UNION ALL
    SELECT DATEFROMPARTS(YEAR(c.dtAbertura), MONTH(c.dtAbertura), 1), COUNT(*)
    FROM ReqConcluida c WITH(NOLOCK)
    WHERE c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
    GROUP BY DATEFROMPARTS(YEAR(c.dtAbertura), MONTH(c.dtAbertura), 1)
) x
GROUP BY x.mes
ORDER BY x.mes;
```

Granularidade do resultado: uma linha por mês com ao menos uma requisição.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | mes | qtd_requisicoes |
    |---|---|
    | 2030-01-01 | 120 |
    | 2030-02-01 | 98 |

## 5. Regras aplicadas

- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas para qualquer volume histórico.

## Veja também

- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
