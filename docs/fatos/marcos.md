---
gerado: sincronizacao
---
# Fato: marcos da requisição


## 1. O que mede

As datas que marcam a vida da requisição: abertura, prazo previsto, início real, primeira resposta, último registro de quem atende e encerramento. Com elas se responde "estourou o prazo?", "quando foi a primeira resposta?" e "há quanto tempo está atrasada?".

## 2. Granularidade

Uma linha por requisição, nas colunas de datas de `Req` (aberta) e de `ReqConcluida` (encerrada). Os nomes e os tipos são os mesmos nas duas tabelas.

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `Req` | `dtFimReal` vazia |
| Encerrada | `ReqConcluida` | `dtFimReal` preenchida |
| Ambas | `vwReq`, `vwReqTotal` | trazem `dtAbertura`, `dtIniPrev`, `dtIniReal`, `dtFimPrev`, `dtFimReal` e `sla` das duas tabelas ([Fato: requisição](requisicao.md)); `dtResposta`, `dtUltHistADO`, `flgForaSLA` e `SLAOrig` ficam em `Req` ∪ `ReqConcluida` |

- **Quem grava.** O produto grava as datas ao longo da vida da requisição:
  - na abertura, são gravados `dtIniPrev`, `dtFimPrev`, `sla` e `SLAOrig`, e `dtAbertura` recebe a data e hora do momento pelo valor padrão da coluna. No tempo decorrido, `dtFimPrev` é calculado a partir do `sla`, e também na ação `ENVAV`; no prazo informado ou sem atividade, o `sla` é calculado a partir das datas; detalhe em [Prioridade e SLA](../dimensoes/prioridade-sla.md);
  - a cada registro de histórico, `dtUltHistADO` e `dtResposta` são atualizadas;
  - o reagendamento e a alteração de prazo zeram `dtResposta` quando o novo `dtIniPrev` é posterior ao anterior;
  - o início da requisição grava `dtIniReal`, assim como o planejamento do fluxo e a ação de replanejamento, e a repriorização a zera;
  - o encerramento grava `dtFimReal` e, em seguida, move a linha para `ReqConcluida`.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `dtAbertura` | abertura da requisição: a gravação da abertura não a informa e a coluna recebe `getdate()` do valor padrão; sempre preenchida (`NOT NULL`) | data e hora |
| `dtIniPrev` | início previsto; sempre preenchida (`NOT NULL`) | data e hora |
| `dtFimPrev` | fim previsto, o prazo; sempre preenchida (`NOT NULL`) | data e hora |
| `sla` / `Sla` | minutos de calendário entre `dtIniPrev` e `dtFimPrev` no calendário do grupo (`Req.sla` e `ReqConcluida.Sla`); `SLAOrig` recebe o mesmo `sla` na abertura e é regravado com o novo `sla` na categorização; a alteração de prazo não o altera | minutos do calendário |
| `dtIniReal` | início real: o início da requisição grava a data e hora do momento em que é acionado pela primeira vez, se a coluna ainda está vazia e a requisição tem `idFrmStatus` preenchido; várias ações o acionam (por exemplo a execução de ações e a inclusão de documento); o planejamento do fluxo e a ação de replanejamento gravam a data planejada quando a coluna está vazia, e a repriorização a zera; pode estar vazia | data e hora |
| `dtResposta` | primeira resposta: a data do primeiro histórico de um participante de atendimento (`ADO`, `RESP`, `APROV`, `SHADO`, `SAN`, `SHANTE`), exceto na ação `CAT`; o reagendamento e a alteração de prazo a zeram quando o novo `dtIniPrev` é posterior ao anterior, e um histórico offline com data anterior a faz recuar; pode estar vazia | data e hora |
| `dtUltHistADO` | `dtFimReqHist` do último histórico gravado de um participante de atendimento (mesma lista de papéis; a ação `CAT` também atualiza); pode estar vazia | data e hora |
| `dtFimReal` | encerramento; vazia na aberta | data e hora |
| `flgForaSLA` | flag mantida pela criação do plano de alertas e pelo processamento de alertas (ver [Prioridade e SLA](../dimensoes/prioridade-sla.md)); uma atualização de versão do produto também a regrava com 0 | |

`dtResposta` e `dtUltHistADO` são atualizadas a cada registro de histórico. O valor gravado é `dtFimReqHist` do histórico; se um registro com data anterior chega depois (histórico offline), `dtResposta` recua para essa data. `dtUltHistADO` recebe o `dtFimReqHist` de cada registro sem comparar datas, de modo que um registro com data anterior também a faz recuar. As colunas `dtResposta`, `dtIniReal` e `dtUltHistADO` podem estar vazias: nem toda requisição teve atendimento registrado.

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Tempo | `idReq` → `ReqTime` / `ReqTimeConcluida`, que medem os intervalos entre estes marcos ([Tempo da requisição](tempo-requisicao.md)) |
| Calendário | o calendário do grupo (`Grupo.idCan`) mede `sla` ([Calendário](../dimensoes/tempo-calendario.md)) |
| Grupo | `idGruAtual` → `Grupo.idGru` ([R-requisicao-05](requisicao.md)) |

## 6. Regras de uso

#### R-marcos-01: Leia a primeira resposta em `dtResposta`. {#r-marcos-01}
A coluna é gravada pelo produto no primeiro histórico de um participante de atendimento, exceto na ação `CAT`; o reagendamento e a alteração de prazo a zeram quando o novo `dtIniPrev` é posterior ao anterior. A leitura se apoia em duas definições (decisão do produto): a regra de gravação de `dtResposta` descrita acima é a definição oficial de primeira resposta, e a "primeira ação" do atendimento é a mesma data; `dtIniReal` é um marco diferente (R-marcos-05).
Receita: [tempo até a primeira resposta](../receitas/tempo-ate-primeira-resposta.md)

#### R-marcos-02: Compare `dtFimPrev` com `dtFimReal` nas encerradas e com o momento da consulta nas abertas para saber se estourou o prazo. {#r-marcos-02}
Estourou o prazo é `dtFimPrev` anterior a `dtFimReal` (encerradas) ou ao momento da consulta (abertas). Definição: decisão do produto.
Receita: [SLA por grupo](../receitas/sla-por-grupo.md)

#### R-marcos-03: Leia o encerramento em `dtFimReal`, que só existe nas encerradas. {#r-marcos-03}
O encerramento grava `dtFimReal` e a requisição passa a `ReqConcluida`. Na aberta, a coluna é vazia.
Receita: [SLA por grupo](../receitas/sla-por-grupo.md)

#### R-marcos-04: Leia o prazo pelas datas; `flgForaSLA` é gravada pelo plano de alertas e regravada com 0 por uma atualização de versão do produto. {#r-marcos-04}
`Req.flgForaSLA` é gravada ao criar ou recriar o plano de alertas, com 1 se `dtFimPrev` já passou, e no processamento de alertas, com 1 quando o alerta de 100% é processado e 0 nos demais; uma atualização de versão do produto também a regrava com 0. Ela mostra o resultado da última dessas gravações; no encerramento, a flag é copiada para `ReqConcluida.flgForaSla`.
Receita: [atrasadas agora](../receitas/atrasadas-agora.md)

#### R-marcos-05: Leia o início real em `dtIniReal` e a primeira resposta em `dtResposta` como marcos diferentes. {#r-marcos-05}
`dtIniReal` é gravada no início da requisição, na primeira vez em que ele é acionado (com `idFrmStatus` preenchido), pelo planejamento do fluxo e pela ação de replanejamento, e zerada na repriorização; `dtResposta` é gravada no primeiro histórico de atendimento, sem a ação `CAT`. As duas colunas são independentes e podem ter datas diferentes na mesma requisição. Decisão do produto: `dtIniReal` é um marco diferente da primeira resposta e da primeira ação, que seguem `dtResposta`.
Receita: [tempo até a primeira resposta](../receitas/tempo-ate-primeira-resposta.md)

#### R-marcos-06: Leia as datas como hora local dos servidores da instalação, sem fuso gravado. {#r-marcos-06}
As colunas de data são `DATETIME`, sem fuso, e as gravações não convertem para UTC. Dois relógios entram nas datas.

O relógio do servidor de banco grava `dtAbertura`, pelo valor padrão da coluna, `dtIniReal`, no início do atendimento, `dtFimReal`, quando o encerramento não informa a data, `ReqHistorico.dtRegistro`, pelo valor padrão da coluna, e `dtCalc`. A exceção é `dtIniReal` gravada pelo planejamento do fluxo ou pela ação de replanejamento, que recebe a data planejada e não o relógio do banco. O relógio do servidor que executa o produto define o "agora" da abertura, que vira `dtIniPrev` quando a abertura não informa a data e serve de base para `dtFimPrev`, e grava `dtFimReqHist` do histórico; no registro offline, vale a data informada. `dtResposta` e `dtUltHistADO` recebem esse `dtFimReqHist` (seção 4).

Para converter para UTC, use o fuso nomeado da instalação (o identificador IANA, como America/Sao_Paulo), com as regras históricas dele. Um deslocamento fixo, como o que `SELECT SYSDATETIMEOFFSET()` mostra hoje, erra as datas dos períodos de horário de verão, que vigorou no Brasil até fevereiro de 2019. Na volta do horário de verão, uma hora se repete, e as datas gravadas nessa hora ficam ambíguas.

Para saber se os dois relógios estão no mesmo fuso, compare `dtRegistro` com `dtFimReqHist` em `ReqHistorico`: as duas são gravadas no mesmo comando de inclusão, a primeira pelo relógio do banco e a segunda pelo relógio do produto. Rode `SELECT TOP 5 DATEDIFF(MINUTE, dtFimReqHist, dtRegistro), COUNT(*) FROM ReqHistorico GROUP BY DATEDIFF(MINUTE, dtFimReqHist, dtRegistro) ORDER BY COUNT(*) DESC`. Os registros offline e o primeiro histórico de uma requisição agendada ou offline levam outra data e espalham as diferenças; o valor mais frequente mostra a relação entre os relógios. Perto de 0, os dois relógios coincidem; um múltiplo estável de 60 minutos indica fusos diferentes; poucos minutos indicam desvio entre os relógios. Quando os relógios diferem, as datas do histórico e do prazo ficam deslocadas das de abertura, início real e encerramento por essa diferença.
Receita: [SLA por grupo](../receitas/sla-por-grupo.md)

#### R-marcos-07: Nas abertas, leia o "agora" uma vez por carga e grave-o junto com o resultado. {#r-marcos-07}
As receitas de abertas comparam `dtFimPrev` com `GETDATE()`, a data e hora do servidor de banco no momento em que a consulta roda (R-marcos-02). Num pipeline, esse momento é o horário da carga: "atrasada agora" e "no prazo" valem para aquele instante, e duas cargas dos mesmos dados dão resultados diferentes. Leia `GETDATE()` uma vez no início da carga, guarde o valor numa variável (`@agora`), use-a no lugar de `GETDATE()` em todas as receitas da carga e grave-a numa coluna do resultado; recalcule o atraso no destino a partir dessa coluna, e não do relógio da ferramenta de destino, que pode estar em outro fuso (R-marcos-06). O prazo calculado na abertura parte do relógio do servidor que executa o produto, e `@agora` vem do relógio do banco (R-marcos-06): uma diferença entre os dois relógios desloca o corte de "atrasada" e de "no prazo" pelo mesmo valor. Os tempos gravados das abertas são de outro instante, `dtCalc` ([Tempo da requisição](tempo-requisicao.md), R-tempo-requisicao-07). Para escolher o que recarregar e em que ordem ler abertas e encerradas, siga R-abertas-e-encerradas-01 e R-abertas-e-encerradas-02 ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).
Receita: [atrasadas agora](../receitas/atrasadas-agora.md)

## 7. Views recomendadas

- `vwReq` e `vwReqTotal` trazem `dtAbertura`, `dtIniPrev`, `dtIniReal`, `dtFimPrev`, `dtFimReal` e `sla` numa só consulta, uma linha por requisição ([Fato: requisição](requisicao.md)). Para `dtResposta`, `dtUltHistADO`, `flgForaSLA` e `SLAOrig`, leia `Req` ∪ `ReqConcluida`.

## 8. Receitas

- [Tempo até a primeira resposta](../receitas/tempo-ate-primeira-resposta.md)
- [SLA por grupo](../receitas/sla-por-grupo.md)
- [Atrasadas agora](../receitas/atrasadas-agora.md)

## Veja também

- [Tempo da requisição](tempo-requisicao.md)
- [Fato: requisição](requisicao.md)
- [Prioridade e SLA](../dimensoes/prioridade-sla.md)
