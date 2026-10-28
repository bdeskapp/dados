---
gerado: sincronizacao
---
# Receita: tempo total por requisição


## 1. Pergunta e indicador

- **Pergunta:** qual o tempo total que o BDesk gravou para cada requisição, aberta ou encerrada, aberta num período, junto com os tempos de resposta e de atendimento gravados para ela?
- **Indicador:** tempo total da requisição = `tTotalCal` (minutos de calendário). `tRespCal` (até a primeira resposta) e `tAtendCal` (atendimento) acompanham como medidas próprias, e `tTotal` traz o total em minutos corridos.

## 2. Definição usada

- Os tempos da requisição estão em `ReqTime` (aberta) e `ReqTimeConcluida` (encerrada), uma linha por requisição ([Fato: tempo da requisição](../fatos/tempo-requisicao.md)).
- No cálculo atual, `tTotalCal` é o tempo ativo mais o tempo congelado calculados sobre o histórico: o cálculo percorre os trechos do histórico com status, soma o tempo em status que conta no SLA e o tempo em status que não conta, e acrescenta o intervalo do último registro até `dtCalc`. As colunas `tAtivoCal` e `tFreezeCal` que a atualização de `ReqTime` grava são só de atendimento, e a linha de `ReqTimeConcluida` calculada pelo cálculo de tempos de encerradas grava `tFreezeCal` de atendimento e `tAtivoCal` do histórico; por isso `tTotalCal` pode diferir da soma das colunas gravadas `tAtivoCal` e `tFreezeCal`. As linhas calculadas por versões anteriores do produto ficam como histórico (decisão do produto) e têm outra fórmula: nelas `tTotalCal` é `tRespCal + tAtendCal`, e no cálculo atual é `tAtivoCal + tFreezeCal`. Para separar as duas, use `dtCalc`, o momento do cálculo da linha, que a consulta devolve: compare `tTotalCal` com `tRespCal + tAtendCal` e com `tAtivoCal + tFreezeCal`, por faixa de `dtCalc` ([R-tempo-requisicao-04](../fatos/tempo-requisicao.md)).
- Nem toda aberta tem linha em `ReqTime`, e algumas linhas de `ReqTimeConcluida` têm tempos vazios. Por isso os dois ramos usam `LEFT JOIN`, e a requisição sem tempo aparece com os tempos vazios.
- O período filtra por `dtAbertura`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas. Para um estado só, mantenha o ramo correspondente.

```sql
SELECT r.idReq, 0 AS encerrada, r.dtAbertura, t.dtCalc,
       t.tRespCal, t.tAtendCal, t.tTotalCal, t.tTotal
FROM Req r WITH(NOLOCK)
    LEFT JOIN ReqTime t WITH(NOLOCK) ON t.idReq = r.idReq
WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
UNION ALL
SELECT c.idReq, 1, c.dtAbertura, t.dtCalc,
       t.tRespCal, t.tAtendCal, t.tTotalCal, t.tTotal
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN ReqTimeConcluida t WITH(NOLOCK) ON t.idReq = c.idReq
WHERE c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0;
```

Granularidade do resultado: uma linha por requisição.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | encerrada | dtAbertura | dtCalc | tRespCal | tAtendCal | tTotalCal | tTotal |
    |---|---|---|---|---|---|---|---|
    | 2001 | 0 | 2030-03-01 | 2030-03-05 | 120 | 300 | 420 | 1500 |
    | 2002 | 1 | 2030-03-02 | 2030-03-03 | 30 | 90 | 120 | 400 |
    | 2003 | 0 | 2030-03-04 | | | | | |

## 5. Regras aplicadas

- [R-tempo-requisicao-01](../fatos/tempo-requisicao.md): some abertas e encerradas pelas duas tabelas de tempo.
- [R-tempo-requisicao-02](../fatos/tempo-requisicao.md): nem toda aberta tem linha em `ReqTime`; use `LEFT JOIN` para listar todas.
- [R-tempo-requisicao-03](../fatos/tempo-requisicao.md): leia os tempos `...Cal` em minutos do calendário do grupo e os sem sufixo em minutos corridos.

## Veja também

- [Fato: tempo da requisição](../fatos/tempo-requisicao.md)
- [Receita: tempo de atendimento por grupo](tempo-atendimento-por-grupo.md)
- [Marcos da requisição](../fatos/marcos.md)
