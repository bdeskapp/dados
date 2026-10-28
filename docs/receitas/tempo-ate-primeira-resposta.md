---
gerado: sincronizacao
---
# Receita: tempo até a primeira resposta


## 1. Pergunta e indicador

- **Pergunta:** quanto tempo as requisições, abertas e encerradas, abertas num período, levaram até a primeira resposta?
- **Indicador:** tempo até a primeira resposta = `tRespCal` (minutos de calendário entre o início previsto, `dtIniPrev`, e `dtResposta`), por requisição, e a média por mês de abertura. Requisições com `dtResposta` anterior a `dtIniPrev` têm `tRespCal` igual a 0 e entram na média como zero.

## 2. Definição usada

- A primeira resposta é a data `dtResposta`, gravada pelo produto no primeiro histórico de um participante de atendimento (`ADO`, `RESP`, `APROV`, `SHADO`, `SAN`, `SHANTE`), exceto na ação `CAT`. A data não é definitiva: um registro de atendimento posterior com `dtFimReqHist` anterior à `dtResposta` gravada (o caso do registro offline) a substitui, e as ações de reagendar e de alterar o prazo a zeram quando o novo início previsto é posterior ao anterior. A primeira ação registrada pelo atendimento coincide com essa data ([Marcos da requisição](../fatos/marcos.md)).
- `tRespCal` mede de `dtIniPrev` até `dtResposta` no calendário do grupo que respondeu, ou no calendário padrão quando quem respondeu não é um grupo.
- Quando `dtResposta` é anterior a `dtIniPrev`, `tResp` fica negativo e `tRespCal` fica 0, porque o cálculo só soma enquanto a data base é menor que o fim. Esses casos entram na média como zero (decisão do produto: a resposta antes do início do prazo conta como zero, porque o produto grava `tRespCal = 0`), e a coluna qtd_resposta_antes_do_inicio do bloco por mês diz quantos há em cada mês.
- Sem `dtResposta`, a aberta guarda `tRespCal = 0` e a encerrada guarda o tempo até `dtFimReal`. Por isso a receita mantém só as requisições com `dtResposta` preenchida.
- Na aberta, `tResp` e `tRespCal` refletem `dtIniPrev` e `dtResposta` do último cálculo, gravado em `dtCalc` ([R-tempo-requisicao-06](../fatos/tempo-requisicao.md)). O registro que grava `dtResposta` recalcula os tempos da requisição logo depois, então a resposta entra no cálculo. `dtResposta` recebe a data do registro (`dtFimReqHist`) e `dtCalc` a hora do banco no cálculo (`GETDATE()`); por isso `dtCalc` anterior a `dtResposta` não indica cálculo feito antes da resposta. Se `dtIniPrev` mudar depois do cálculo, a linha guarda o tempo antigo até o próximo cálculo.
- Na encerrada, a linha de `ReqTimeConcluida` é a cópia da última linha de `ReqTime` no encerramento, ou o cálculo de tempos da encerrada quando ela não tem linha. O cálculo feito com `dtFimReal` preenchida usa `dtFimReal` como fim; `dtCalc` mostra qual cálculo ficou gravado. Com `dtResposta` preenchida, `tRespCal` mede de `dtIniPrev` até `dtResposta`, mesmo quando `dtResposta` é posterior a `dtFimReal`.
- A aberta com `dtResposta` e sem linha em `ReqTime` aparece com os tempos vazios (`LEFT JOIN`); a média ignora os valores vazios.
- O período filtra por `dtAbertura`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas. Para um estado só, mantenha o ramo correspondente.

```sql
SELECT r.idReq, 0 AS encerrada, r.dtAbertura, r.dtIniPrev, r.dtResposta,
       t.tRespCal, t.tResp
FROM Req r WITH(NOLOCK)
    LEFT JOIN ReqTime t WITH(NOLOCK) ON t.idReq = r.idReq
WHERE r.dtResposta IS NOT NULL
  AND r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
UNION ALL
SELECT c.idReq, 1, c.dtAbertura, c.dtIniPrev, c.dtResposta,
       t.tRespCal, t.tResp
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN ReqTimeConcluida t WITH(NOLOCK) ON t.idReq = c.idReq
WHERE c.dtResposta IS NOT NULL
  AND c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0;
```

Granularidade do resultado: uma linha por requisição.

Média por mês de abertura, somando abertas e encerradas, com a quantidade de requisições cuja resposta é anterior ao início previsto (contam como zero na média):

```sql
SELECT x.mes, COUNT(*) AS qtd_requisicoes, COUNT(x.tRespCal) AS qtd_com_tempo,
       AVG(CAST(x.tRespCal AS float)) AS media_resposta_min_cal,
       SUM(CASE WHEN x.dtResposta < x.dtIniPrev THEN 1 ELSE 0 END) AS qtd_resposta_antes_do_inicio
FROM (
    SELECT DATEFROMPARTS(YEAR(r.dtAbertura), MONTH(r.dtAbertura), 1) AS mes, t.tRespCal, r.dtResposta, r.dtIniPrev
    FROM Req r WITH(NOLOCK)
        LEFT JOIN ReqTime t WITH(NOLOCK) ON t.idReq = r.idReq
    WHERE r.dtResposta IS NOT NULL
      AND r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
    UNION ALL
    SELECT DATEFROMPARTS(YEAR(c.dtAbertura), MONTH(c.dtAbertura), 1), t.tRespCal, c.dtResposta, c.dtIniPrev
    FROM ReqConcluida c WITH(NOLOCK)
        LEFT JOIN ReqTimeConcluida t WITH(NOLOCK) ON t.idReq = c.idReq
    WHERE c.dtResposta IS NOT NULL
      AND c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
) x
GROUP BY x.mes
ORDER BY x.mes;
```

Granularidade do resultado: uma linha por mês.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | mes | qtd_requisicoes | qtd_com_tempo | media_resposta_min_cal | qtd_resposta_antes_do_inicio |
    |---|---|---|---|---|
    | 2030-01-01 | 120 | 120 | 35.5 | 4 |
    | 2030-02-01 | 98 | 97 | 41.0 | 0 |

## 5. Regras aplicadas

- [R-tempo-requisicao-05](../fatos/tempo-requisicao.md): leia o tempo até a primeira resposta em `tRespCal` e mantenha só as requisições com `dtResposta`.
- [R-marcos-01](../fatos/marcos.md): `dtResposta` é a primeira resposta.
- [R-tempo-requisicao-02](../fatos/tempo-requisicao.md): a aberta sem linha de tempo aparece com os tempos vazios.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas.

## Veja também

- [Marcos da requisição](../fatos/marcos.md)
- [Fato: tempo da requisição](../fatos/tempo-requisicao.md)
