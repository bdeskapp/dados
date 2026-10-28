# Carga incremental

Esta página mostra como levar os dados da requisição para o seu destino, seja um lakehouse, um data warehouse ou uma réplica de leitura, sem perder nem duplicar linhas. Ela vale para qualquer pipeline e não depende de ferramenta.

!!! warning "Não há coluna de alteração"
    As oito tabelas da requisição e dos tempos não registram a data de alteração da linha. No esquema publicado, `Req`, `ReqConcluida`, as tabelas de tempo e as de tempo por status não têm coluna `rowversion` nem data de alteração, e as colunas de data que existem são marcos de negócio ou o momento do cálculo. O log de alterações da requisição (`RequisicaoLog`) também não serve de marca: ele cobre só parte das colunas de `Req` e nada das encerradas nem das tabelas de tempo. Por isso, recarregue as abertas por inteiro a cada carga e reconcilie as encerradas com cargas completas periódicas ([R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01)). As colunas de cada tabela estão no dicionário, por exemplo em [dbo.Req](../dicionario/dbo-req.md), [dbo.ReqConcluida](../dicionario/dbo-reqconcluida.md) e [dbo.ReqTime](../dicionario/dbo-reqtime.md).

## O encerramento muda a requisição de tabela

A requisição aberta fica em `Req`. Quando ela é encerrada, o produto copia a linha para `ReqConcluida` e apaga a de `Req`, com a mesma `idReq` ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)). No seu pipeline, isso aparece como:

- uma **exclusão** em `Req`;
- uma **inclusão** em `ReqConcluida`, com a mesma `idReq`.

O que você pode contar como certo, pela mesma regra:

- A única inclusão em `Req` é a abertura, e cada abertura recebe uma `idReq` nova.
- A única exclusão em `Req` é a do encerramento.
- Nada apaga linhas de `ReqConcluida`. A requisição encerrada não é reaberta: a passagem acontece uma vez só.

Para achar as encerradas novas, compare as `idReq` de `ReqConcluida` com as que você já tem no destino. Não filtre por `dtFimReal` posterior à última carga: a data do encerramento pode ser informada e ficar anterior à sua última carga ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)).

!!! tip "A requisição que sumiu das abertas"
    Uma `idReq` que estava em `Req` na carga anterior e não está mais foi encerrada, e deve aparecer em `ReqConcluida`. Ela só fica fora das duas leituras se `ReqConcluida` foi lida antes de `Req`, ou se uma leitura com `WITH(NOLOCK)` pulou a linha. Na ordem recomendada, `Req` primeiro, o pior caso é a duplicata ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)). Se mesmo assim a requisição faltar, a próxima carga corrige, porque as abertas são recarregadas por inteiro e as encerradas novas são achadas pela `idReq` (veja [chaves de deduplicação](#chaves-de-deduplicacao)).

### As tabelas dependentes acompanham a requisição

As tabelas ligadas à requisição também têm uma versão aberta e uma encerrada, e o encerramento copia as linhas de uma para a outra. A soma das duas é o histórico completo ([R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01), [R-tempo-por-grupo-02](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-02) e [R-tempo-por-status-01](../fatos/tempo-por-status.md#r-tempo-por-status-01)). Há exceções que o seu pipeline precisa conhecer:

- **Participação e despesa sem cadastro completo** não são copiadas para a encerrada e deixam de existir nas duas tabelas ([R-participacao-02](../fatos/participacao.md#r-participacao-02), [R-apontamento-e-despesas-05](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-05) e [removidas no encerramento, sem cópia](../mapa/abertas-e-encerradas.md#removidas-no-encerramento-sem-copia)).
- **Apontamentos de uma requisição de fluxo** continuam nas tabelas abertas, mesmo com a requisição já em `ReqConcluida`, até o encerramento da requisição raiz do fluxo ([R-apontamento-e-despesas-05](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-05)). Não deduza o estado da requisição pela tabela do apontamento.
- Algumas tabelas são apagadas no encerramento sem cópia. A lista está em [Abertas e encerradas: removidas no encerramento, sem cópia](../mapa/abertas-e-encerradas.md#removidas-no-encerramento-sem-copia).

### Os demais pares: histórico, participação, mensagens e outros

Os pares fora das oito tabelas da requisição e dos tempos seguem outra regra ([R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03)):

- **Abertas:** perdem as linhas no encerramento. Recarregue-as por inteiro a cada carga.
- **Encerradas:** nada apaga linhas delas, e só o encerramento inclui linhas. Traga-as só por acréscimo, pelas `idReq` das encerradas novas ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)), sem filtro de data. As datas dessas tabelas são do evento, e não da entrada da linha.
- **Apontamentos de requisições em fluxo:** entram em `ReqApontConcluida` e `ReqApontAprovConcluida` só no encerramento da requisição raiz. Nessas duas tabelas, traga as `idReqApont` que ainda faltam no destino.
- **Colunas que mudam depois do encerramento:** só duas. `ReqPartConcluida.dtUltimoAcesso` é regravada quando alguém abre a requisição encerrada, e `ReqDocConcluida.flgExcluido` passa a 1 quando o arquivo vencido é apagado. Atualize essas colunas por `idReqPart` e `idDoc` nas cargas completas periódicas, ou deixe-as fora do destino.

Assim, entre as encerradas desses pares, só `ReqPartConcluida`, `ReqDocConcluida` e os apontamentos de requisições em fluxo precisam de reconciliação.

## Pares aberta e encerrada

Estes são os pares em que o encerramento copia a linha da aberta para a encerrada. A coluna da direita diz o que a encerrada traz a mais; o detalhe está em [Abertas e encerradas](../mapa/abertas-e-encerradas.md).

| Aberta | Encerrada | O que a encerrada traz a mais |
|---|---|---|
| `Req` | `ReqConcluida` | colunas de retrato do encerramento, como o nome do grupo e a classificação |
| `ReqParticipante` | `ReqPartConcluida` | `dsPapel` e `nmPart`; só as participações com cadastro completo |
| `ReqHistorico` | `ReqHistConcluida` | rótulos gravados: `dsGru`, `dsAcao`, `dsMotivo`, `dsSta`, `nmPersona`, `nmUsu`, `nmPart`, `dsTitulo` |
| `ReqUltHist` | `ReqUltHistConcluida` | nenhuma coluna a mais |
| `ReqHistAcesso` | `ReqHistAcessoConcluida` | nenhuma coluna a mais |
| `ReqMensagem` | `ReqMsgConcluida` | `dsTpMsg` |
| `ReqMsgAcesso` | `ReqMsgAcessoConcluida` | nenhuma coluna a mais |
| `ReqDocumento` | `ReqDocConcluida` | nenhuma coluna a mais |
| `ReqDocAcesso` | `ReqDocAcessoConcluida` | nenhuma coluna a mais |
| `ReqDespesa` | `ReqDespConcluida` | `nmUsu`, `dsCatDesp`, `dsItemDesp`, `RazaoSocial`; só as despesas com cadastro completo |
| `ReqApontamento` | `ReqApontConcluida` | nenhuma coluna a mais |
| `ReqApontAprov` | `ReqApontAprovConcluida` | `nmUsuAprov` |
| `ReqRecat` | `ReqRecatConcluida` | nenhuma coluna a mais |
| `ReqAprov` | `ReqAprovConcluida` | nenhuma coluna a mais |
| `ReqStatus` | `ReqStatusConcluida` | nenhuma coluna a mais |
| `ReqTime` | `ReqTimeConcluida` | nenhuma coluna a mais |
| `ReqTimeAdo` | `ReqTimeAdoConcluida` | nenhuma coluna a mais |
| `ReqKB` | `ReqKBConcluida` | nenhuma coluna a mais |
| `ReqProblema` | `ReqProblemaConcluida` | nenhuma coluna a mais |
| `ReqMinuta` | `ReqMinutaConcluida` | nenhuma coluna a mais |
| `ReqMinutaHistorico` | `ReqMinutaHistConcluida` | nenhuma coluna a mais |
| `ReqPartRep` | `ReqPartRepConcluida` | nenhuma coluna a mais |

Três colunas existem só na aberta: `ReqHistorico.flgCalc`, `ReqStatus.flgUtilizado` e `ReqTime.flgErro`. Ao unir os dois lados no destino, preencha essas colunas como vazias no lado encerrado.

### Tabelas sem par

Estas tabelas guardam as linhas de abertas e de encerradas juntas e não mudam de tabela no encerramento: `ReqAvaliacao`, `ReqVinculada`, `ReqVinculadaRef`, `PesqRespCab` e `DadValor`. Para elas, o encerramento não gera exclusão nem inclusão. Para saber se a requisição de uma linha está aberta ou encerrada, junte com `Req` e com `ReqConcluida` ([R-vinculos-02](../fatos/vinculos.md#r-vinculos-02) e [R-dados-adicionais-02](../fatos/dados-adicionais.md#r-dados-adicionais-02)).

## As tabelas de tempo são recalculadas por substituição

Os tempos são gravados, e o cálculo **apaga e recria** a linha da requisição em `ReqTime` e em `ReqTimeAdo`. A linha também some quando o calendário ou o grupo é alterado, e só volta no próximo cálculo ([R-tempo-requisicao-02](../fatos/tempo-requisicao.md#r-tempo-requisicao-02) e [R-tempo-calendario-04](../dimensoes/tempo-calendario.md#r-tempo-calendario-04)). Na tabela de tempo por status, a passagem atual de cada aberta recebe valores provisórios a cada execução do lote diário ([R-tempo-por-status-04](../fatos/tempo-por-status.md#r-tempo-por-status-04)).

Consequências para o pipeline:

- Trate `ReqTime`, `ReqTimeAdo` e `ReqStatus` como um retrato: a cada carga, **substitua** o conjunto inteiro no destino ([R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01)). Uma carga que só inclui e atualiza deixa no destino linhas que já sumiram da origem.
- A aberta sem linha em `ReqTime` deve aparecer no destino com os tempos vazios, e não com os tempos da carga anterior ([R-tempo-requisicao-02](../fatos/tempo-requisicao.md#r-tempo-requisicao-02)).
- Grave `dtCalc` junto com os tempos. A defasagem de cada linha é o horário da carga menos `dtCalc` ([R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07)).
- Evite rodar a carga durante o lote diário de recálculo. O lote apaga e inclui de novo a linha de cada aberta, sem transação, e uma carga nesse intervalo deixa de encontrar a linha. Na agenda que o produto instala, o lote faz parte de uma rotina que começa às 00h30 do servidor de banco; confirme a agenda vigente com o administrador ([R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07)).
- O prazo de uma aberta também muda: `dtFimPrev` é recalculado na alteração de prazo, na alteração de prioridade que recalcula o SLA, no congelamento definitivo e na alteração de calendário ou de grupo ([R-tempo-calendario-04](../dimensoes/tempo-calendario.md#r-tempo-calendario-04), [Calendário de atendimento, seção 3](../dimensoes/tempo-calendario.md#3-como-a-requisicao-aponta-para-ele) e [Marcos, seção 3](../fatos/marcos.md#3-tabelas)). Compare sempre com o `dtFimPrev` da carga atual; nunca reaproveite o prazo de uma carga anterior.
- Nas encerradas, os tempos são os do encerramento. Mesmo assim, uma encerrada pode ganhar a linha de tempo depois, com `dtCalc` igual a `dtFimReal`: um filtro por `dtCalc` posterior à última carga deixa essa linha de fora ([R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01)).

## Janela de reprocessamento

Sem coluna de alteração, a janela de reprocessamento é definida pelo estado da requisição, e não por uma data:

| Conjunto | O que fazer a cada carga | Regra |
|---|---|---|
| Abertas (`Req`, `ReqTime`, `ReqTimeAdo`, `ReqStatus`) | trazer inteiras e substituir no destino | [R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01) |
| Encerradas novas | trazer as `idReq` de `ReqConcluida` que ainda faltam no destino | [R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02) |
| Encerradas já carregadas | refazer de tempos em tempos a carga completa de `ReqConcluida`, `ReqTimeConcluida`, `ReqTimeAdoConcluida` e `ReqStatusConcluida` | [R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01) |
| Abertas dos demais pares | trazer inteiras e substituir no destino | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| Encerradas dos demais pares | acrescentar as linhas das `idReq` encerradas novas e, nos apontamentos, as `idReqApont` que faltam; nas cargas completas periódicas, atualizar só `ReqPartConcluida.dtUltimoAcesso` e `ReqDocConcluida.flgExcluido` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |

A reconciliação das encerradas é necessária porque a encerrada ainda muda depois do encerramento. O título e a descrição das encerradas de um fluxo são regravados quando a requisição raiz os altera, e outras colunas, como `SlaReal`, também são regravadas ([R-abertas-e-encerradas-01](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-01)). A periodicidade da carga completa é sua: quanto maior o intervalo, por mais tempo o destino pode divergir da origem nessas colunas. Depois de cada reconciliação, recalcule os indicadores dos períodos já fechados.

Dois cuidados valem para toda carga:

- **O "agora" das abertas.** Leia o horário uma vez no início da carga, use-o em todas as consultas no lugar da data e hora do servidor e grave-o numa coluna do resultado ([R-marcos-07](../fatos/marcos.md#r-marcos-07)). Detalhes em [acesso e leitura](acesso-e-leitura.md).
- **O fuso e os dois relógios.** As datas são hora local, sem fuso gravado, e vêm de dois relógios ([R-marcos-06](../fatos/marcos.md#r-marcos-06)). O servidor que executa o produto grava `dtFimReqHist` do histórico, e por isso `dtResposta` e `dtUltHistADO`, e é a base de `dtIniPrev` e `dtFimPrev`. O servidor de banco grava `dtAbertura`, `dtIniReal`, `dtFimReal` (quando o encerramento não informa a data) e `dtCalc`. Se os dois estão em fusos diferentes, as datas de um grupo ficam deslocadas das do outro. A regra descreve uma consulta que compara os dois relógios no histórico; rode-a uma vez por instalação. Para converter para UTC, use o fuso nomeado da instalação, com as regras históricas de horário de verão, e não um deslocamento fixo.

## Chaves de deduplicação

Use estas chaves para mesclar a parte aberta e a encerrada no destino e para descartar repetições:

| Tabelas | Chave | Regra |
|---|---|---|
| `Req` / `ReqConcluida` | `idReq` | [R-requisicao-01](../fatos/requisicao.md#r-requisicao-01) |
| `ReqTime` / `ReqTimeConcluida` | `idReq` | [R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01) |
| `ReqTimeAdo` / `ReqTimeAdoConcluida` | `idReq`, `idReqPart` | [R-tempo-por-grupo-03](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-03) |
| `ReqStatus` / `ReqStatusConcluida` | `idReqStatus` (uma linha por passagem) | [R-tempo-por-status-02](../fatos/tempo-por-status.md#r-tempo-por-status-02) |
| `ReqHistorico` / `ReqHistConcluida` | `idReqHist` (único por evento) | [R-eventos-historico-05](../fatos/eventos-historico.md#r-eventos-historico-05) |
| `ReqParticipante` / `ReqPartConcluida` | `idReqPart` | [R-participacao-06](../fatos/participacao.md#r-participacao-06) |
| `ReqApontamento` / `ReqApontConcluida` | `idReqApont` | [R-apontamento-e-despesas-04](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-04) |
| `ReqMensagem` / `ReqMsgConcluida` | `idReqMsg` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqDocumento` / `ReqDocConcluida` | `idDoc` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqDespesa` / `ReqDespConcluida` | `idReqDesp` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqAprov` / `ReqAprovConcluida` | `idReqAprov` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqMinutaHistorico` / `ReqMinutaHistConcluida` | `idReqMinutaHist` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| tabelas de acesso (`ReqHistAcesso`, `ReqMsgAcesso`, `ReqDocAcesso` e as encerradas) | o item acessado, `idReqPart` e `dtInicio` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqUltHist`, `ReqProblema`, `ReqMinuta` e as encerradas | `idReq` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `ReqKB` / `ReqKBConcluida` | `idReq`, `idKB` | [R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03) |
| `DadValor` | `idDadVal`, a chave primária | [Dados adicionais, seção 2](../fatos/dados-adicionais.md#2-granularidade) |

Duas encerradas não usam a chave da aberta ([R-abertas-e-encerradas-03](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-03)):

- `ReqRecatConcluida` recebe um `idReqRecat` novo no encerramento, diferente do da aberta. Ligue-a à requisição por `idReq` e ao histórico por `idReqHist`.
- `ReqPartRepConcluida` não tem chave primária.

Em `DadValor`, a chave natural do valor (`idQQ`, `idDadCon`, `nSeq`, `flgAgenda`) não é imposta por nenhum índice único. Use `idDadVal` para mesclar e deduplicar, e trate a chave natural como uma checagem de qualidade, não como chave ([Dados adicionais, seção 2](../fatos/dados-adicionais.md#2-granularidade)).

O encerramento move a requisição numa só transação. Mesmo assim, duas leituras separadas, uma leitura com `WITH(NOLOCK)` ou cargas independentes de uma réplica podem ver a mesma `idReq` nas duas tabelas ou em nenhuma ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)). Deduplique sempre por `idReq` e, quando a mesma requisição aparecer nos dois lados, fique com a linha de `ReqConcluida`: o encerramento é definitivo.

!!! tip "Leia as abertas primeiro"
    Leia `Req` antes de `ReqConcluida`. Na ordem inversa, uma requisição encerrada entre as duas leituras não aparece em nenhum dos lados naquela carga. Na ordem recomendada, o pior caso é a duplicata, que a chave `idReq` resolve. Outra saída é ler as duas tabelas no mesmo snapshot (veja [acesso e leitura](acesso-e-leitura.md#o-que-withnolock-significa)).
