---
gerado: sincronizacao
---
# Receita: tempo da abertura ao encerramento por categoria


## 1. Pergunta e indicador

- **Pergunta:** quanto tempo as requisições encerradas num período levaram da abertura ao encerramento, por categoria?
- **Indicador:** duas medidas, lado a lado, por categoria:
  - **tempo corrido** = média, em minutos de relógio, do intervalo entre `dtAbertura` e `dtFimReal`;
  - **tempo de calendário** = média de `ReqTimeConcluida.tTotalCal`, o tempo total que o BDesk gravou para a requisição, em minutos do calendário do grupo.

## 2. Definição usada

- **Encerradas:** as linhas de `ReqConcluida` cujo `dtFimReal` cai no período. `dtFimReal` só existe nas encerradas ([R-marcos-03](../fatos/marcos.md)).
- **Recorte das canceladas:** a receita mede as encerradas que não foram canceladas, o mesmo conjunto de [SLA por grupo](sla-por-grupo.md), e descarta o status de código `CL` (`FormStatus.idSta` → `Status.cdSta`, [R-status-fase-04](../dimensoes/status-fase.md)). Para medir também as canceladas, retire do `WHERE` a condição que descarta o status `CL`.
- **Categoria:** a do retrato gravado no encerramento, `ReqConcluida.idCat` ([R-classificacao-03](../dimensoes/classificacao.md)). O total por categoria soma por `idCat`; por isso a receita agrupa só por `idCat`. O rótulo `dsCat` também é retrato, e o mesmo `idCat` pode ter mais de um rótulo gravado (a categoria renomeada entre dois encerramentos): qtd_rotulos conta os rótulos distintos do grupo, e `dsCat` mostra o maior deles em ordem binária, que distingue acento e maiúscula e por isso escolhe sempre a mesma grafia. A requisição encerrada sem atividade tem `idCat` vazio e entra na linha de categoria vazia.
- **Tempo corrido:** `DATEDIFF(minute, dtAbertura, dtFimReal)`, contado em viradas de minuto do relógio, sem calendário. `dtAbertura` é a abertura e `dtFimReal` o encerramento ([Marcos](../fatos/marcos.md)). Quando `dtFimReal` é anterior a `dtAbertura`, o intervalo sai negativo e entra assim na média.
- **Tempo de calendário:** `tTotalCal` de `ReqTimeConcluida` ([R-tempo-requisicao-04](../fatos/tempo-requisicao.md)), em minutos do calendário do grupo ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md)). No encerramento, a linha de `ReqTime` da requisição é copiada para `ReqTimeConcluida`. A ligação é `LEFT JOIN`: `ReqTimeConcluida` tem linhas com os tempos vazios, e a média ignora esses casos; qtd_com_tempo_calendario diz quantas requisições entram nessa média.
- **As duas medidas não se comparam termo a termo.** Elas diferem em quatro pontos:
  - **Início:** o tempo corrido começa em `dtAbertura`; `tTotalCal` começa no primeiro trecho do histórico com status e com participante `ADO`, não na abertura.
  - **Fim:** o tempo corrido termina em `dtFimReal`; `tTotalCal` termina em `dtCalc`, o momento do cálculo, que vale `dtFimReal` quando ela está preenchida e o momento da execução quando não está.
  - **Unidade:** o tempo corrido é minuto de relógio; `tTotalCal` conta só as faixas de horário do calendário do grupo do ADO de cada trecho, ou do calendário padrão quando o ADO não é grupo; `tTotalCal` soma ainda o intervalo do último registro do histórico (`dtUltHist`) até `dtCalc`, calculado com o calendário do grupo atual da requisição (`idGruAtual`) ou, quando ele é nulo, com o calendário padrão.
  - **Composição de `tTotalCal`:** o cálculo atual soma o tempo em status que conta no SLA e o tempo em status que não conta sobre o histórico, mais o intervalo de `dtUltHist` até `dtCalc`, que entra em um dos dois conforme a requisição estava ativa, mas as colunas `tAtivoCal` e `tFreezeCal` que a atualização de `ReqTime` grava são só de atendimento, de modo que `tTotalCal` pode não ser a soma das duas colunas gravadas ([R-tempo-requisicao-04](../fatos/tempo-requisicao.md)). As linhas calculadas por versões anteriores do produto ficam como histórico (decisão do produto) e têm outra fórmula: nelas `tTotalCal` é `tRespCal + tAtendCal`, e no cálculo atual é `tAtivoCal + tFreezeCal`. A média mistura as duas fórmulas quando o período tem linhas das versões antigas; para separá-las, acrescente ao `WHERE` um corte em `dtCalc` e compare `tTotalCal` com cada soma, por faixa de `dtCalc`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. As médias são convertidas em `decimal(18,2)` antes do cálculo, para não truncar a divisão inteira, e saem com duas casas decimais. Só encerradas, porque `dtFimReal` só existe nelas.

```sql
SELECT c.idCat, MAX(c.dsCat COLLATE Latin1_General_BIN2) AS dsCat, COUNT(DISTINCT c.dsCat COLLATE Latin1_General_BIN2) AS qtd_rotulos,
       COUNT(*) AS qtd_encerradas,
       CAST(AVG(CAST(DATEDIFF(minute, c.dtAbertura, c.dtFimReal) AS decimal(18,2))) AS decimal(18,2)) AS media_min_corridos,
       COUNT(t.tTotalCal) AS qtd_com_tempo_calendario,
       CAST(AVG(CAST(t.tTotalCal AS decimal(18,2))) AS decimal(18,2)) AS media_min_calendario
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN ReqTimeConcluida t WITH(NOLOCK) ON t.idReq = c.idReq
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
WHERE ISNULL(s.cdSta, '') <> 'CL'
  AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
GROUP BY c.idCat
ORDER BY dsCat;
```

Granularidade do resultado: uma linha por categoria (`idCat`), mais uma linha para as requisições sem categoria.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idCat | dsCat | qtd_rotulos | qtd_encerradas | media_min_corridos | qtd_com_tempo_calendario | media_min_calendario |
    |---|---|---|---|---|---|---|
    | | | 0 | 15 | 2400.00 | 14 | 700.50 |
    | 1001 | Categoria Exemplo A | 1 | 120 | 1500.25 | 120 | 480.10 |
    | 1002 | Categoria Exemplo B | 2 | 40 | 300.00 | 39 | 95.75 |

## 5. Regras aplicadas

- [R-classificacao-03](../dimensoes/classificacao.md): a categoria de uma encerrada vem do retrato `ReqConcluida.idCat`, e o total por categoria soma por `idCat`.
- [R-marcos-03](../fatos/marcos.md): o encerramento é `dtFimReal`, que só existe nas encerradas.
- [R-tempo-requisicao-03](../fatos/tempo-requisicao.md): `tTotalCal` está em minutos do calendário do grupo.
- [R-tempo-requisicao-04](../fatos/tempo-requisicao.md): o tempo total gravado é `tTotalCal`, com outra composição nas linhas antigas.
- [R-status-fase-04](../dimensoes/status-fase.md): a cancelada se lê pelo código `CL`.

## Veja também

- [Fato: tempo da requisição](../fatos/tempo-requisicao.md)
- [Dimensão: classificação](../dimensoes/classificacao.md)
- [Receita: tempo total por requisição](tempo-total-por-requisicao.md)
- [Receita: volume por classificação](volume-por-classificacao.md)
