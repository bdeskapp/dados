# Calendário e tempos

O prazo e boa parte dos tempos do Bdesk são medidos em **minutos de calendário**: só contam os minutos dentro do horário de atendimento do grupo. Esta página descreve como essa contagem funciona, para você refazer a conta fora do banco, por exemplo para medir um atraso até o horário da carga. As tabelas e colunas estão em [Dimensão: calendário de atendimento](../dimensoes/tempo-calendario.md) e em [Fato: tempo da requisição](../fatos/tempo-requisicao.md).

## Duas unidades

- As colunas de tempo terminadas em `Cal`, como `tTotalCal` e `tAtrasoCal`, estão em minutos do calendário do grupo. As colunas sem esse sufixo, como `tTotal`, estão em minutos corridos ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)).
- O `sla` da requisição, que é o intervalo entre o início e o fim previstos, também está em minutos de calendário ([R-prioridade-sla-04](../dimensoes/prioridade-sla.md#r-prioridade-sla-04)).

Não compare nem some colunas das duas unidades.

## O que forma um calendário

Cada calendário (`CalendarioNome`) tem linhas de regra em `Calendario`, de dois tipos ([Calendário de atendimento](../dimensoes/tempo-calendario.md)):

- **Dia da semana:** a linha diz em quais faixas de horário aquele dia da semana tem atendimento. São até três faixas por dia, cada uma com início e fim no formato `HH:mm`. O fim `23:59` vale até a meia-noite ([Calendário de atendimento, seção 2](../dimensoes/tempo-calendario.md#2-estrutura)).
- **Data específica:** a linha vale para uma data do ano. Quando existe uma linha de data para o dia, ela prevalece sobre a linha do dia da semana. Uma linha de data sem horário marca o dia como não útil ([R-tempo-calendario-02](../dimensoes/tempo-calendario.md#r-tempo-calendario-02)).

### Feriados

Os feriados só contam depois de copiados para o calendário. O cadastro de feriados (`Feriado`) não entra na conta: o produto copia os feriados escolhidos para `Calendario`, como linhas de data sem horário, quando alguém faz essa cópia na tela. Os feriados móveis não entram nessa cópia ([R-tempo-calendario-03](../dimensoes/tempo-calendario.md#r-tempo-calendario-03)).

!!! warning "Leia só a tabela de regras do calendário"
    Para refazer a conta, use apenas as linhas de `Calendario`. Um feriado cadastrado em `Feriado` que não foi copiado para o calendário conta como dia normal.

### Dia da semana

O cálculo compara o dia da semana gravado na linha de regra (`diaSemana`) com o número do dia que o SQL Server devolve para a data (`DATEPART(dw)`) na sessão que faz o cálculo. É esse número da sessão que depende da configuração de primeiro dia da semana (`SET DATEFIRST`) ([Calendário de atendimento, seção 2](../dimensoes/tempo-calendario.md#2-estrutura)). Antes de levar as regras para outro motor, confira com o administrador da instalação qual configuração vale na sessão que calcula e converta a numeração para a do seu motor.

## Como os minutos de calendário são contados

Cada coluna `...Cal` é um intervalo, como de `dtIniPrev` a `dtResposta` em `tRespCal`, ou uma soma de intervalos contados um a um, como os trechos do histórico e o intervalo final até `dtCalc`. O arredondamento acontece em cada intervalo, e não no total ([R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08)). Para um intervalo:

1. Trunque o início e o fim ao minuto, descartando os segundos.
2. Percorra o intervalo dia a dia. Para cada dia, escolha a regra: a linha de data específica, se houver; senão, a linha do dia da semana ([R-tempo-calendario-02](../dimensoes/tempo-calendario.md#r-tempo-calendario-02)).
3. Se a regra do dia não tem horário, o dia não soma nada.
4. Senão, conte os minutos de relógio do intervalo que caem dentro das faixas do dia. O minuto de início da faixa conta e o minuto de fim não conta: a faixa de 08:00 a 18:00 tem 600 minutos, de 08:00 a 17:59. O fim de faixa 23:59 vale como a meia-noite seguinte, de modo que o minuto 23:59 conta.
5. O valor do intervalo é a soma dos dias, em minutos.

Por exemplo, de 08:10:50 a 08:12:10, dentro do expediente, contam 2 minutos: 08:10 e 08:11 ([R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08)).

Duas situações somam 1 minuto à conta acima ([R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08)):

- **Intervalo curto no mesmo minuto.** Um intervalo de 1 a 59 segundos que começa e termina no mesmo minuto de relógio conta 1 minuto, se esse minuto cai numa faixa, mas só no calendário de um grupo. No calendário padrão, usado para o participante que não é grupo e para a requisição sem grupo atual, o mesmo intervalo conta 0. O intervalo curto que atravessa uma virada de minuto conta 1 minuto nos dois calendários, pela regra geral.
- **Fim às 23:59:00 em ponto.** O intervalo é contado até a meia-noite seguinte, e o minuto 23:59 conta, se cai numa faixa.

!!! tip "Diferença esperada"
    Seguindo esses passos, a sua conta reproduz o valor gravado. Se você somar os segundos exatos dentro das faixas e dividir por 60, cada intervalo fica a menos de 1 minuto do valor gravado, mais o minuto das duas situações acima; numa requisição, essas diferenças se acumulam trecho a trecho ([R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08)).

## Qual calendário cada medida usa

A requisição não aponta direto para o calendário: o caminho é pelo grupo, em `Grupo.idCan`. Na falta de grupo, vale o calendário padrão da instalação, guardado em `Parametro` na linha `idPar = 15` ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)). O grupo usado muda conforme a medida ([R-tempo-calendario-01](../dimensoes/tempo-calendario.md#r-tempo-calendario-01)):

| Medida | Calendário |
|---|---|
| Atraso e avanço (`tAtrasoCal`, `tAvancoCal`, `tAtrasoRealCal`, `tAvancoRealCal`) e o trecho final, do último registro até `dtCalc` | o do grupo atual da requisição (`idGruAtual`); sem grupo atual, o padrão |
| Tempo ativo e congelado (`tAtivoCal`, `tFreezeCal`) | o do grupo que atendia em cada trecho do histórico, quando o participante é um grupo; o padrão nos demais casos |
| Tempo até a primeira resposta (`tRespCal`) | o de quem respondeu, com a mesma regra; na encerrada sem resposta, o do grupo atual ([R-tempo-requisicao-05](../fatos/tempo-requisicao.md#r-tempo-requisicao-05)) |
| Prazo (`sla`) | o do grupo do momento do cálculo: na abertura, na categorização ou na ação que recalculou o prazo |

!!! note "O prazo pode estar em outro calendário"
    O `sla` segue o calendário do grupo do momento do cálculo ([R-tempo-calendario-01](../dimensoes/tempo-calendario.md#r-tempo-calendario-01)). Depois de um direcionamento sem recálculo do prazo, ele continua medido no calendário do grupo anterior ([Calendário de atendimento, seção 3](../dimensoes/tempo-calendario.md#3-como-a-requisicao-aponta-para-ele)). Por isso, não recalcule o `sla` com o calendário do grupo atual e espere o mesmo valor.

## Quando o calendário muda

A alteração de um calendário ou de um grupo recalcula as requisições abertas afetadas: o prazo é refeito e as linhas de tempo da requisição são apagadas até o próximo cálculo ([R-tempo-calendario-04](../dimensoes/tempo-calendario.md#r-tempo-calendario-04)). Leve em conta que:

- uma conta refeita com o calendário de hoje pode divergir de um tempo gravado antes da alteração;
- logo depois da alteração, a aberta pode ficar sem linha de tempo ([R-tempo-requisicao-02](../fatos/tempo-requisicao.md#r-tempo-requisicao-02)).

Se você copia as regras do calendário para o destino, recarregue-as a cada carga, junto com as abertas.

## Calcular "até agora" fora do banco

Os tempos gravados de uma aberta valem para o instante `dtCalc`, e não para o horário da consulta ([R-tempo-requisicao-06](../fatos/tempo-requisicao.md#r-tempo-requisicao-06)). Para medir, por exemplo, o atraso de uma aberta até o horário da carga:

1. Capture o horário da carga uma vez e grave-o junto com o resultado ([R-marcos-07](../fatos/marcos.md#r-marcos-07)).
2. Compare `dtFimPrev` com esse horário para saber se o prazo estourou ([R-marcos-02](../fatos/marcos.md#r-marcos-02)).
3. Para o atraso em minutos de calendário, aplique a contagem acima ao intervalo entre `dtFimPrev` e o horário da carga, no calendário do grupo atual (`idGruAtual`), que é o que o produto usa no atraso. Se a requisição não tem grupo atual, use o calendário padrão, o da linha `idPar = 15` de `Parametro` ([R-tempo-calendario-01](../dimensoes/tempo-calendario.md#r-tempo-calendario-01) e [R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)).
4. Use o mesmo fuso das datas gravadas: elas são hora local dos servidores da instalação, e o relógio do seu pipeline pode estar em outro fuso. O prazo parte do relógio do servidor que executa o produto, e o horário da carga lido no banco vem do relógio do servidor de banco: se os dois relógios diferem, o corte de "atrasada" se desloca pela mesma diferença ([R-marcos-06](../fatos/marcos.md#r-marcos-06) e [R-marcos-07](../fatos/marcos.md#r-marcos-07)).

!!! warning "O atraso refeito não substitui o gravado"
    O atraso gravado em `tAtrasoCal` depende também de a requisição estar num status que conta prazo ([Fato: tempo da requisição, seção 4](../fatos/tempo-requisicao.md#4-colunas-chave)). A conta acima mede o intervalo no calendário e não reproduz essa condição. Deixe claro no seu indicador qual das duas medidas ele usa.

### Levar `tTotalCal` até o horário da carga

Para uma aberta sem registro de histórico nem alteração de grupo ou de calendário depois de `dtCalc` ([R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08)):

```text
tTotalCal até agora = tTotalCal gravado
                    + minutos de calendário entre dtCalc e o horário da carga
```

- Conte os minutos com os passos acima, com `dtCalc` e o horário da carga truncados ao minuto.
- Use o calendário do grupo atual (`idGruAtual`) ou, sem grupo atual, o calendário padrão (`idPar = 15`). É o mesmo calendário do intervalo final que o produto grava ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)).
- O resultado coincide com o de um recálculo feito naquele horário, ou fica 1 minuto acima quando o intervalo final gravado caiu numa das duas situações que somam 1 minuto.
- O horário da carga e `dtCalc` vêm do mesmo relógio, o do servidor de banco ([R-marcos-06](../fatos/marcos.md#r-marcos-06) e [R-marcos-07](../fatos/marcos.md#r-marcos-07)).

Se houve registro de histórico ou mudança de grupo ou de calendário depois de `dtCalc`, a fórmula não vale: espere o próximo cálculo ([R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07)).
