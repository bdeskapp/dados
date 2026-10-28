---
gerado: sincronizacao
---
# Fato: tempo da requisição


## 1. O que mede

Quanto tempo cada requisição levou até a primeira resposta, em atendimento e no total, e quanto passou do prazo ou sobrou dele. Cada medida existe em duas unidades: minutos corridos e minutos do calendário do grupo.

## 2. Granularidade

Uma linha por requisição, em `ReqTime` (aberta) ou `ReqTimeConcluida` (encerrada). `idReq` é a chave nas duas tabelas e não se repete entre elas. Nem toda requisição aberta tem linha em `ReqTime`: a alteração de calendário ou de grupo apaga a linha, e a aberta fica sem ela até um novo cálculo de tempos recriá-la: o próximo cálculo da própria requisição ou o lote diário; a rotina que completa as faltantes também a recria, mas só quando é executada manualmente (seção 3).

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `ReqTime` | uma linha por requisição que já teve os tempos calculados |
| Encerrada | `ReqTimeConcluida` | copiada de `ReqTime` no encerramento; a requisição encerrada sem status (`idFrmStatus` nulo) não tem linha (ver "Encerrada", abaixo) |
| Ambas | `ReqTime` e `ReqTimeConcluida` | somadas por `UNION ALL` (R-tempo-requisicao-01) |

- **Quem grava.** Os tempos são **gravados**, não calculados na leitura. O cálculo de tempos apaga e recria a linha da requisição em `ReqTime` e em `ReqTimeAdo`. Ele roda:
  - a cada registro de histórico;
  - no encerramento, antes de a linha ser copiada para `ReqTimeConcluida`;
  - em consultas de tempos da requisição aberta.
- **Lote.** Uma vez por dia, por rotina agendada, o cálculo roda em lote sobre as abertas sem linha em `ReqTime` e as que têm `dtCalc` em um dia de calendário anterior ao de hoje; o critério conta viradas de dia, não 24 horas.
- **Completar as faltantes.** Uma rotina de complemento percorre as abertas com status e sem linha em `ReqTime` e calcula os tempos de cada uma. Nem o produto nem a rotina agendada a chamam: ela só roda quando alguém a executa manualmente.
- **Quando a linha some.** A alteração de calendário ou de grupo apaga a linha da requisição em `ReqTime` e em `ReqTimeAdo`. A linha volta no próximo cálculo.
- **Atualidade.** `dtCalc` é o momento do cálculo: a data e hora do início do cálculo quando `dtFimReal` está vazia, e a própria `dtFimReal` quando está preenchida, inclusive no cálculo das encerradas.
- **Encerrada.** A linha de `ReqTimeConcluida` é copiada de `ReqTime` no encerramento, e só existe quando a requisição tem linha em `ReqTime` nesse momento. A requisição sem status (`idFrmStatus` nulo) encerra sem linha: o cálculo de tempos só percorre requisições com status, e o cálculo manual das encerradas, descrito a seguir, também exige status. A encerrada com status e sem linha em `ReqTimeConcluida`, quando existe, só a ganha se alguém executar manualmente o cálculo das encerradas, que calcula a linha à parte: pela rotina de complemento, na opção das encerradas, ou por um script avulso de correção. O encerramento grava `ReqConcluida.SlaReal` com o `tTotalCal`; esse cálculo manual regrava a coluna com o `tTotalCal` que calcula.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReq` | requisição | |
| `dtCalc` | momento do cálculo | data e hora |
| `tResp` / `tRespCal` | da data prevista de início (`dtIniPrev`) até a primeira resposta (`dtResposta`); sem resposta, a aberta guarda 0 e a encerrada vai até `dtFimReal` | minutos corridos / minutos do calendário |
| `tAtend` / `tAtendCal` | tempo de atendimento: soma, sobre `ReqTimeAdo`, do tempo ativo e do tempo em status que não conta SLA | minutos corridos / minutos do calendário |
| `tTotal` / `tTotalCal` | tempo total: o cálculo percorre os trechos do histórico a partir do primeiro histórico com status e com participante `ADO`, ignorando os históricos com `idFrmStatus` nulo e os sem linha em `ReqParticipante` para `idReqPartADO`, não a partir de `dtIniPrev`, e soma o tempo ativo e o tempo em status que não conta SLA, mais o intervalo do último registro até `dtCalc`; nas linhas calculadas por versões anteriores do produto, `tTotalCal` é `tRespCal + tAtendCal` (decisão do produto; ver R-tempo-requisicao-04) | minutos corridos / minutos do calendário |
| `tAtraso` / `tAtrasoCal` | quanto passou de `dtFimPrev`: até `dtCalc` quando a aberta está em status que conta SLA; nos demais casos, até a maior `dtFimReqHist` entre os históricos em status que conta SLA (`flgContaSLA = 1`); nesses casos, com `dtCalc` depois de `dtFimPrev`, `tAtraso` fica negativo quando esse último histórico é anterior a `dtFimPrev` | minutos corridos / minutos do calendário |
| `tAtrasoReal` / `tAtrasoRealCal` | quanto passou de `dtFimPrev` até `dtUltHistADO` (último registro de quem atende) | minutos corridos / minutos do calendário |
| `tAvanco` / `tAvancoCal` | encerrada antes de `dtFimPrev`: tempo entre `dtFimReal` e `dtFimPrev`; `tAvanco` e `tAvancoReal`, e também `tAvancoCal` e `tAvancoRealCal`, só são calculados com `dtResposta` preenchida; sem ela as quatro ficam 0 | minutos corridos / minutos do calendário |
| `tAvancoReal` / `tAvancoRealCal` | o mesmo, medido a partir de `dtUltHistADO` | minutos corridos / minutos do calendário |
| `tAtivo` / `tAtivoCal`, `tFreeze` / `tFreezeCal` | tempo em status que conta no SLA (`FormStatus.flgContaSLA = 1`) e em status que não conta; ver regra R-tempo-requisicao-04 | minutos corridos / minutos do calendário |

Unidades. As colunas sem sufixo estão em minutos corridos. As colunas `...Cal` estão em minutos do calendário do grupo; ver [Calendário](../dimensoes/tempo-calendario.md). Nas colunas sem sufixo, intervalos de 1 a 59 segundos contam 1 minuto; a contagem dos minutos de calendário, inclusive a dos intervalos curtos, está em R-tempo-requisicao-08.

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` ([Fato: requisição](requisicao.md)) |
| Atendimento por grupo | `ReqTimeAdo` e `ReqTimeAdoConcluida`, por `idReq` ([Tempo por grupo](tempo-por-grupo.md)) |
| Tempo por status | `ReqStatus` e `ReqStatusConcluida`, por `idReq` ([Tempo por status](tempo-por-status.md)) |
| Datas de prazo e resposta | `Req` e `ReqConcluida` ([Marcos](marcos.md)) |
| Calendário | o calendário do grupo (`Grupo.idCan`) ([Calendário](../dimensoes/tempo-calendario.md)) |

## 6. Regras de uso

#### R-tempo-requisicao-01: Some `ReqTime` e `ReqTimeConcluida` para qualquer tempo histórico. {#r-tempo-requisicao-01}
`ReqTime` guarda só as requisições abertas e `ReqTimeConcluida` as encerradas, sem `idReq` em comum.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-requisicao-02: Parta de `Req` com `LEFT JOIN ReqTime` quando a lista precisa conter todas as abertas. {#r-tempo-requisicao-02}
A linha de `ReqTime` nasce quando os tempos da requisição são calculados e some quando um calendário ou grupo é alterado; a aberta sem linha aparece com os tempos vazios. Abertas com status e sem linha em `ReqTime` ocorrem: a alteração de calendário ou de grupo apaga a linha da requisição, e a rotina que completa as faltantes, que só roda quando é executada manualmente, a recria apenas para a aberta com `idFrmStatus` preenchido.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-requisicao-03: Leia os campos `...Cal` em minutos do calendário do grupo e os campos sem sufixo em minutos corridos. {#r-tempo-requisicao-03}
O calendário (dias úteis e faixas de horário) vem de `Grupo.idCan` e, na falta de grupo, do calendário padrão do `Parametro` de `idPar = 15`. O grupo varia por coluna. `tAtivo`, `tFreeze` e `tTotal` (= `tAtivo` + `tFreeze`) vêm do percurso de todo o histórico da requisição: em cada trecho do histórico usam o grupo do ADO do trecho quando ele é do tipo Grupo (`idTpPapel = 2`) e o calendário padrão nos demais tipos. `tAtend` vem do percurso do histórico de atendimento e usa o mesmo critério por trecho, somando as linhas de `ReqTimeAdo`. O intervalo final (do último registro até `dtCalc`) usa `Req.idGruAtual`, com o calendário padrão quando ele é nulo, e entra em `tTotal`, em `tAtivo`/`tFreeze` e em `tAtend` (via `ReqTimeAdo`). `tAtraso`, `tAtrasoReal`, `tAvanco` e `tAvancoReal` usam `Req.idGruAtual`, com o calendário padrão quando `idGruAtual` é nulo.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-requisicao-04: Leia o tempo total em `tTotalCal` e o desmembramento ativo e congelado do atendimento em `ReqTimeAdo`. {#r-tempo-requisicao-04}
No cálculo atual, `tTotalCal` é a soma do tempo ativo e do tempo congelado calculados sobre o histórico: o cálculo percorre os trechos do histórico a partir do primeiro e soma o intervalo final até `dtCalc`. As colunas gravadas `tAtivo`/`tAtivoCal` e `tFreeze`/`tFreezeCal` dependem de como a linha foi gravada: quando a linha é criada em `ReqTime`, trazem os tempos do histórico inteiro; quando uma linha existente é atualizada, trazem os tempos do atendimento, a soma de `ReqTimeAdo`; e na linha calculada à parte para a encerrada, `tAtivo` é do histórico inteiro e `tFreeze` é do atendimento. Por isso `tTotalCal` pode diferir da soma das colunas gravadas `tAtivoCal` e `tFreezeCal`. As linhas calculadas por versões anteriores do produto ficam como histórico (decisão do produto) e têm outra fórmula: nelas `tTotalCal` é `tRespCal + tAtendCal`, enquanto o cálculo atual grava `tAtivoCal + tFreezeCal`. Para separar as duas, use `dtCalc`, o momento em que cada linha foi calculada: compare `tTotalCal` com `tRespCal + tAtendCal` e com `tAtivoCal + tFreezeCal`, por faixa de `dtCalc`; as linhas das versões antigas fecham com a primeira soma. O tempo congelado é o tempo em status que não contam prazo (`FormStatus.flgContaSLA` igual a 0), gravado em `tFreezeCal` de `ReqTime` e de `ReqTimeAdo` (decisão do produto); o congelamento definitivo de `FormStatus.tpCongelamento` é o mecanismo que estende o prazo, e não a fonte desse tempo. `tAtendCal` é a soma das linhas de `ReqTimeAdo` da requisição.
Receita: [tempo de atendimento por grupo](../receitas/tempo-atendimento-por-grupo.md)

#### R-tempo-requisicao-05: Leia o tempo até a primeira resposta em `tRespCal` e mantenha só as requisições com `dtResposta` preenchida. {#r-tempo-requisicao-05}
Sem `dtResposta`, a aberta guarda `tRespCal = 0` e a encerrada guarda o tempo até `dtFimReal`. Com `dtResposta` anterior a `dtIniPrev`, o produto grava `tRespCal = 0`, porque a contagem de minutos do calendário só soma enquanto a data base é menor que o fim; a resposta antes do início do prazo conta como zero (decisão do produto). O calendário de `tRespCal` é o do ADO (`idReqPartADO`) do histórico cuja `dtFimReqHist` é igual a `dtResposta`: se esse participante é do tipo Grupo, vale o calendário do grupo; nos demais tipos, como usuário, vale o calendário padrão. Na encerrada sem resposta, vale o calendário de `idGruAtual`.
Receita: [tempo até a primeira resposta](../receitas/tempo-ate-primeira-resposta.md)

#### R-tempo-requisicao-06: Leia a atualidade do tempo em `dtCalc`. {#r-tempo-requisicao-06}
O tempo está gravado no último cálculo. Uma aberta mostra o tempo de `dtCalc`, não o do momento da consulta; para "agora" use as datas previstas ([Marcos](marcos.md)).
Receita: [atrasadas agora](../receitas/atrasadas-agora.md)

#### R-tempo-requisicao-07: Grave `dtCalc` junto com os tempos de cada aberta e meça a defasagem como a diferença entre o horário da carga e `dtCalc`. {#r-tempo-requisicao-07}
O horário da carga é o `@agora` de R-marcos-07, lido do relógio do servidor de banco, o mesmo relógio que grava `dtCalc`. Os tempos de uma aberta são recalculados por evento: a cada registro de histórico, nas consultas de tempos da requisição e no encerramento (seção 3). Sem evento, a linha só muda no lote, que recalcula as abertas com `dtCalc` em um dia de calendário anterior ao da execução. A rotina agendada que o produto instala começa às 00h30 do servidor de banco, todos os dias, e o recálculo é o segundo passo dela; a agenda vigente em cada instalação pode ser outra. O lote grava em `dtCalc` a data e hora do início dele, a mesma para todas as linhas. Com a agenda instalada, uma linha calculada entre 00h00 e o início do lote passa pela execução do mesmo dia sem ser recalculada, e a defasagem chega a 24h30 mais a duração do primeiro passo e do lote até alcançar a linha; com outra agenda, ou com a rotina parada, a linha fica como está até o próximo evento. Durante o lote, a linha de cada aberta é apagada e incluída de novo, sem transação: uma carga nesse intervalo deixa de encontrá-la, como acontece com a aberta sem linha da R-tempo-requisicao-02. Por isso a defasagem se mede linha a linha: `@agora` menos `dtCalc`. Nas encerradas, os tempos são os do encerramento: o cálculo roda logo depois de gravar `dtFimReal` e usa `dtFimReal` como `dtCalc`. A aberta sem linha em `ReqTime` fica sem tempos até o próximo cálculo (R-tempo-requisicao-02). Para escolher o que recarregar a cada carga, siga R-abertas-e-encerradas-01 e R-abertas-e-encerradas-02 ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-requisicao-08: Reproduza os minutos de calendário intervalo a intervalo, truncando ao minuto o início e o fim de cada um e contando os minutos de relógio que caem nas faixas do calendário. {#r-tempo-requisicao-08}
Cada campo `...Cal` de `ReqTime`, `ReqTimeAdo` e das encerradas é um intervalo, como de `dtIniPrev` a `dtResposta` em `tRespCal`, ou uma soma de intervalos contados um a um: os trechos do histórico e o intervalo final, do último registro até `dtCalc` (R-tempo-requisicao-03). O arredondamento acontece em cada intervalo, e não no total. Dentro do intervalo, a contagem percorre os dias e, em cada dia, soma a diferença em minutos de relógio entre o início e o fim da interseção do intervalo com cada faixa, sem olhar os segundos. Como as bordas das faixas e a meia-noite caem em minutos inteiros, a divisão por dia e por faixa não altera o resultado: cada intervalo vale o número de minutos de relógio dentro das faixas entre o início truncado ao minuto e o fim truncado ao minuto. Assim, de 08:10:50 a 08:12:10, dentro do expediente, contam 2 minutos (08:10 e 08:11). O minuto de início da faixa (`hInicio1`, `hInicio2`, `hInicio3`) conta e o minuto de fim (`hFim1`, `hFim2`, `hFim3`) não conta: a faixa de 08:00 a 18:00 tem 600 minutos, de 08:00 a 17:59. O fim de faixa 23:59 é lido como a meia-noite seguinte: o minuto 23:59 conta, e a faixa de 00:00 a 23:59 cobre as 24 horas do dia.

Duas situações acrescentam 1 minuto à regra. Primeira: o intervalo de 1 a 59 segundos que começa e termina no mesmo minuto de relógio, quando contado no calendário de um grupo, tem o fim adiado em 1 minuto e conta 1 minuto se esse minuto cai numa faixa; no calendário padrão, usado para o participante que não é do tipo Grupo e para a requisição sem grupo atual, o mesmo intervalo conta 0. O intervalo curto que atravessa uma virada de minuto conta 1 minuto nos dois calendários, pela regra geral. Segunda: o intervalo que termina às 23:59:00 em ponto é contado até a meia-noite seguinte, e o minuto 23:59 conta se cai numa faixa.

Quem soma os segundos exatos de calendário e divide por 60 fica, em cada intervalo, a menos de 1 minuto do valor gravado, mais o minuto das duas situações acima; na requisição, essas diferenças se acumulam trecho a trecho. Para levar `tTotalCal` de uma aberta até o `@agora` da carga (R-marcos-07), sem novo registro de histórico nem alteração de grupo ou de calendário depois do último cálculo, some os minutos do calendário de `idGruAtual` (ou do calendário padrão, sem grupo atual) entre o maior de `dtCalc` e `ReqUltHist.dtUltHist` e o `@agora`, os dois truncados ao minuto. O intervalo final vai da data do último registro, gravada pelo relógio do produto, até `dtCalc`, gravada pelo relógio do banco: quando o relógio do produto está adiantado em relação ao do banco (R-marcos-06), o último registro tem data posterior a `dtCalc`, o intervalo final gravado vale 0, e somar a partir de `dtCalc` contaria a mais a diferença entre os relógios. O intervalo final usa o mesmo calendário, e o resultado fica a no máximo 1 minuto do de um recálculo em `@agora`: 1 minuto acima quando o intervalo final gravado caiu numa das duas situações acima, e 1 minuto abaixo quando é o intervalo do último registro até o `@agora` que cai nelas, como na carga feita no mesmo minuto do último registro ou com `@agora` às 23:59:00 em ponto.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-tempo-requisicao-09: Conte que `tTotal`, `tAtivo` e `tFreeze` perdem minutos quando o relógio do produto está adiantado em relação ao do banco. {#r-tempo-requisicao-09}
O intervalo final do cálculo vai da data do último registro, gravada pelo relógio do produto, até `dtCalc`, que na aberta é a data e hora do banco no início do cálculo (R-marcos-06). Com o relógio do produto adiantado, o último registro tem data posterior a `dtCalc` e o intervalo final em minutos corridos sai negativo, porque é a diferença em minutos, sem piso em zero. Esse valor negativo é somado a `tAtivo` ou a `tFreeze`, conforme o status conte ou não o SLA, e daí a `tTotal`, e também à linha de `ReqTimeAdo` do participante, cuja soma dá `tAtend`. Essas colunas ficam menores que a soma dos trechos do histórico pela diferença entre os relógios, e numa requisição com pouco histórico podem ficar negativas. Nos campos `...Cal`, o mesmo intervalo vale 0, porque a contagem de minutos do calendário só soma enquanto o início é anterior ao fim; por isso, nesse caso, `tTotal` pode ficar abaixo de `tTotalCal`. Leia valor negativo nessas colunas como efeito da diferença de relógios, e não como erro de carga, e prefira os campos `...Cal`, que não perdem minutos por esse motivo (R-tempo-requisicao-03).
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

## 7. Views recomendadas

Esta página recomenda as tabelas `ReqTime` e `ReqTimeConcluida`, somadas por `UNION ALL`. Elas trazem as duas unidades (minutos corridos e minutos do calendário) e a composição de cada coluna descrita acima.

## 8. Receitas

- [Tempo total por requisição](../receitas/tempo-total-por-requisicao.md)
- [Tempo até a primeira resposta](../receitas/tempo-ate-primeira-resposta.md)
- [Atrasadas agora](../receitas/atrasadas-agora.md)

## Veja também

- [Fato: requisição](requisicao.md)
- [Tempo por grupo](tempo-por-grupo.md)
- [Tempo por status](tempo-por-status.md)
- [Marcos da requisição](marcos.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
