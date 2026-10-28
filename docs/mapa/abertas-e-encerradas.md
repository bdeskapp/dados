---
gerado: sincronizacao
---
# Abertas e encerradas


O BDesk guarda a requisição em um de dois estados, e cada estado tem a sua própria família de tabelas. Esta página diz onde está cada requisição, quando ela muda de estado e quais tabelas têm par.

## 1. Dois conjuntos que não se sobrepõem

- `Req` guarda as requisições abertas.
- `ReqConcluida` guarda as requisições encerradas.
- Uma mesma `idReq` está em exatamente uma das duas. O procedimento de encerramento copia a linha para `ReqConcluida` e depois apaga a de `Req`.
- **Volume = abertas + encerradas.** Qualquer contagem histórica soma as duas tabelas, ou usa `vwReq` / `vwReqTotal` (seção 4).
- A requisição cancelada não tem tabela própria: ela está em `Req` ou em `ReqConcluida`, e o cancelamento é um status (código `Status.cdSta` = `CL`, o status seguinte da ação `CANC` vem de `FormTransicao` em cada formulário).

### Estado da tabela e status são conceitos diferentes

- Estado (aberta ou encerrada) é a **tabela** em que a linha está.
- Status é o código `Status.cdSta`, alcançado por `Req.idFrmStatus` → `FormStatus.idSta` → `Status.cdSta`. O mesmo código de status, como `CN`, aparece em requisições das duas tabelas. O texto do rótulo (`Status.dsSta`) é editável por instalação.
- Nas views `vwReq` e `vwReqTotal` existe uma coluna chamada `ReqStatus` com o valor `Aberta` ou `Encerrada`. Ela indica a **tabela de origem** da linha. O nome coincide com o da tabela `ReqStatus` (tempo por status), que é outro objeto.

## 2. Quando a requisição muda de estado

1. A requisição passa para `ReqConcluida` quando chega a um **status terminal**: um status sem transição de saída em `FormTransicao` para o formulário dela. Isso vale para qualquer ação que leve ao status terminal, e não para uma ação específica.
2. No encerramento, o produto grava `Req.dtFimReal`, recalcula os tempos e executa o procedimento de encerramento, que copia a requisição e seus dependentes para as tabelas "Concluida" e apaga as cópias de abertas (seção 3).
3. O status de destino de uma ação depende do formulário: a transição de `FormTransicao` (`idFrmStatusProx`) define o status seguinte de cada ação em cada formulário.
4. Uma requisição com status `CN` ou `CL` continua em `Req` quando aquele status tem transição de saída no formulário dela. Por isso o estado (aberta ou encerrada) se lê pela tabela, e não pelo código do status. `CONC` e `ENC` têm o mesmo efeito (encerram quando levam a status final) e só o rótulo muda (decisão do produto; ver [Ação](../dimensoes/acao.md)).

## 3. Tabelas pareadas

Cada linha abaixo é um par provado de duas formas: as duas tabelas existem no banco e o procedimento de encerramento copia a aberta para a encerrada. O verificador lê os pares no bloco ao fim da seção 5.

| Aberta | Encerrada | O que a encerrada traz a mais |
|---|---|---|
| `Req` | `ReqConcluida` | colunas de retrato do encerramento (seção 5) |
| `ReqParticipante` | `ReqPartConcluida` | `dsPapel` (rótulo do papel no formulário) e `nmPart` (nome do participante), gravados no encerramento; só as participações que passam pelo critério da seção 3.1 |
| `ReqHistorico` | `ReqHistConcluida` | rótulos gravados: `dsGru`, `dsAcao`, `dsMotivo`, `dsSta`, `nmPersona`, `nmUsu`, `nmPart`, `dsTitulo` |
| `ReqUltHist` | `ReqUltHistConcluida` | nenhuma coluna a mais |
| `ReqHistAcesso` | `ReqHistAcessoConcluida` | nenhuma coluna a mais |
| `ReqMensagem` | `ReqMsgConcluida` | `dsTpMsg` (rótulo do tipo de mensagem) |
| `ReqMsgAcesso` | `ReqMsgAcessoConcluida` | nenhuma coluna a mais |
| `ReqDocumento` | `ReqDocConcluida` | nenhuma coluna a mais |
| `ReqDocAcesso` | `ReqDocAcessoConcluida` | nenhuma coluna a mais |
| `ReqDespesa` | `ReqDespConcluida` | `nmUsu`, `dsCatDesp`, `dsItemDesp`, `RazaoSocial`; só as despesas que passam pelo critério da seção 3.1 |
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

Só a aberta tem estas colunas: `ReqHistorico.flgCalc`, `ReqStatus.flgUtilizado` e `ReqTime.flgErro`.

### 3.1 O que o encerramento copia

- `ReqPartConcluida` é preenchida por `INNER JOIN vwParticipante`, que exige linha em `PartTipoPapel` para (`idTpPapel`, `idPart`) e `FormPapel.flgAtivo = 1`. A participação que não passa por esse join não é copiada.
- `ReqDespConcluida` é preenchida com `INNER JOIN` em `Usuario`, `CategoriaDespesa` e `ItemDespesa`. A despesa sem cadastro em alguma dessas tabelas não é copiada. As chaves estrangeiras de categoria e de item (confiáveis) e a de usuário (ativa, não confiável) impedem gravar despesa sem categoria, item ou usuário cadastrado; o `INNER JOIN` só descartaria uma linha gravada antes da chave estrangeira de usuário.
- A parte encerrada das receitas de participação herda esse recorte: a participação que não passa pelo `INNER JOIN vwParticipante` falta nas encerradas. É um limite documentado (decisão do produto).

`ReqPartRep` também é copiada pelo procedimento, para `ReqPartRepConcluida`. `ReqPartRep` é o índice do participante vigente por papel: a cada gravação em `ReqParticipante`, o banco apaga a linha quando `dtFim` está preenchida e a insere quando a participação é vigente, e a leitura do participante (`idPtp`) por requisição e papel usa `ReqPartRep` (aberta) ou `ReqPartRepConcluida` (encerrada).

As tabelas `ReqApontamento` e `ReqApontAprov` (fato [apontamento e despesas](../fatos/apontamento-e-despesas.md)) só são copiadas quando a requisição não pertence a um fluxo (`Req.idFlu` vazio); nas de requisições em fluxo, o procedimento de encerramento não toca nas linhas, que ficam nas tabelas abertas até o encerramento da requisição raiz do fluxo.

### Removidas no encerramento, sem cópia

`LicReserva` (as licenças reservadas são devolvidas a `LicDistrib`), `ReqTimeout`, `ReqPendencia`, `ReqTransTimeout`, `ReqAcaoRequerida` e `ReqPlanoAlerta`: o procedimento apaga as linhas da requisição e não as copia. O mesmo vale para a participação e a despesa que não passam pelos `INNER JOIN` da seção 3.1: o procedimento apaga todas as linhas de `ReqParticipante` e de `ReqDespesa` da requisição, de modo que a linha não copiada deixa de existir nas duas tabelas.

### Tabelas únicas para os dois estados

Estas tabelas não têm par e guardam as linhas de requisições abertas e encerradas juntas. Elas se ligam à requisição pelo `idReq`, salvo `DadValor`:

- `ReqAvaliacao`;
- `ReqVinculada`;
- `ReqVinculadaRef` (`idReq`, `idReqVinculo`);
- `PesqRespCab` (`idReq`; ver [Fato: avaliação e satisfação](../fatos/avaliacao-satisfacao.md));
- `DadValor` (ligada à requisição por `idQQ`; ver [Fato: dados adicionais](../fatos/dados-adicionais.md)).

## 4. Uniões prontas

| View | Cobre | Linha por | Como usar |
|---|---|---|---|
| `vwReq` | abertas e encerradas | requisição | `UNION ALL` de `Req` (com `LEFT JOIN FormStatus`) e `ReqConcluida`. A coluna `ReqStatus` diz a origem da linha. Em `dsSta`, a linha aberta traz o rótulo atual de `FormStatus` e a encerrada traz o rótulo gravado no encerramento |
| `vwReqTotal` | abertas e encerradas | requisição | igual a `vwReq`, com a coluna `dsReq` (descrição) a mais |
| `vwRepUltimaAcao` | abertas e encerradas | requisição com linha em `ReqUltHist` ou `ReqUltHistConcluida` | `UNION ALL` do par `ReqUltHist` / `ReqUltHistConcluida`, com o nome do autor, a ação, `dtAcao` e o motivo ([views recomendadas](../views/views-recomendadas.md)) |
| `vwRepTimeStatus` | abertas e encerradas | passagem de status | `UNION ALL` do par `ReqStatus` / `ReqStatusConcluida`, com `idReq`, `idFrmStatus`, `tStatusCal` e `dtFimStatus` |
| `vwReqAcessoTotal` | abertas e encerradas | requisição × participante com acesso × usuário | `UNION ALL` de `vwReqAcesso` e `vwReqAcessoConcluida`, que leem o par `ReqParticipante` / `ReqPartConcluida` |
| `vwReqApontTotal` | abertas e encerradas | apontamento | `UNION ALL` do par `ReqApontamento` / `ReqApontConcluida`, com as mesmas colunas nos dois lados |
| `vwReqApontAprovTotal` | abertas e encerradas | aprovação de apontamento | `UNION ALL` do par `ReqApontAprov` / `ReqApontAprovConcluida`, com `idReqApont`, `tpAprovacao`, `dtInicio`, `dtFim`, `qtdHoras`, `dtAprovacao` e o aprovador (`idUsuAprov`, `nmUsuAprov`); a view não traz `idReq`, que vem de `ReqApontamento` / `ReqApontConcluida` por `idReqApont` |
| `vwReqDespTotal` | abertas e encerradas | despesa | `UNION ALL` do par `ReqDespesa` / `ReqDespConcluida`, com a coluna `ReqStatus` (`Aberta` ou `Encerrada`) e os rótulos de usuário, categoria, item e fornecedor |

`vwReq` e `vwReqTotal` não filtram: cada view tem tantas linhas quanto `Req` mais `ReqConcluida`.

## 5. A classificação gravada no encerramento

`ReqConcluida` tem colunas de **retrato**, gravadas no momento do encerramento. Com a exceção de `SlaReal`, elas ficam como foram gravadas, mesmo que o cadastro mude depois; `SlaReal` só é regravado depois do encerramento por uma rotina de manutenção executada à mão (linha da coluna, abaixo).

| Coluna | De onde vem no encerramento |
|---|---|
| `dsSta` | `FormStatus.dsSta` |
| `dsAre` | `Area.dsAre` |
| `idTar`, `idCat`, `dsCat`, `idSca`, `dsSca`, `dsTar` | `vwTarefa` (classificação da atividade; `INNER JOIN` com `SubCategoria`, `Categoria`, `Area` e `TipoTarefa`, [Fato: requisição](../fatos/requisicao.md)). O procedimento liga `vwTarefa` a `Req` por `LEFT JOIN` e copia `idTar` da view (`vwTarefa.idTar`): se a atividade não tem linha em `vwTarefa`, a encerrada fica sem `idTar` e sem a classificação |
| `SlaReal` | `ReqTime.tTotalCal` no encerramento. Depois do encerramento, o cálculo de tempos das encerradas regrava a coluna com `tAtivoCal + tFreezeCal`; esse cálculo só roda quando alguém executa a rotina de manutenção que completa os tempos faltantes da encerrada sem linha em `ReqTimeConcluida`, que o produto não agenda nem chama |
| `dsGru` | `Grupo.dsGru` do grupo `idGru` |
| `dsFrmOrigem` | `FormOrigem.dsFrmOrigem` |
| `dsLocSistema` | `Localiza.dsLoc` |
| `nmPat`, `numeroPat`, `seriePat` | `Patrimonio` |
| `dsHie` | `OrgHierarquia.dsHie` |
| `RazaoSocial` | `Empresa.RazaoSocial` |

`Req` tem as colunas `tpAgend` e `idUsuOperacao`, que `ReqConcluida` não tem. `Req` guarda a atividade em `idTar`; a categoria e a subcategoria de uma aberta são alcançadas a partir de `Tarefa`, e as de uma encerrada estão no retrato de `ReqConcluida` (quando a atividade tem linha em `vwTarefa`).


## 6. Regras de uso

#### R-abertas-e-encerradas-01: Recarregue as abertas por inteiro a cada carga e reconcilie as encerradas com cargas completas periódicas, porque as oito tabelas da requisição e dos tempos não registram a data de alteração da linha. {#r-abertas-e-encerradas-01}
`Req`, `ReqConcluida`, `ReqTime`, `ReqTimeConcluida`, `ReqTimeAdo`, `ReqTimeAdoConcluida`, `ReqStatus` e `ReqStatusConcluida` não têm coluna `rowversion` nem data de alteração. As colunas de data dessas oito tabelas são os marcos da requisição em `Req` e `ReqConcluida` (`dtAbertura`, `dtIniPrev`, `dtFimPrev`, `dtIniReal`, `dtFimReal`, `dtResposta`, `dtUltHistADO`), `dtCalc` nas tabelas de tempo e `dtIniStatus`, `dtFimStatus` e `dtUltimoAlerta` nas de tempo por status. Nenhuma delas acompanha toda alteração da linha. `dtCalc` é o momento do último cálculo dos tempos (R-tempo-requisicao-07), e a alteração de calendário ou de grupo apaga a linha da aberta em `ReqTime` e em `ReqTimeAdo` sem deixar rastro. `dtFimReal` é a data de encerramento, do relógio do servidor de banco ou informada no encerramento, e não o momento em que a linha entrou em `ReqConcluida` (R-abertas-e-encerradas-02).

A encerrada ainda muda depois do encerramento. O produto regrava `flgVinc` e `flgDepende` ao criar e ao desfazer vínculos, `idFlu` ao criar a instância de um fluxo, o título e a descrição (`dsTitulo`, `dsReq`) das encerradas de um fluxo quando a requisição raiz do fluxo os altera, e `flgReincidente`; uma atualização de versão e scripts pontuais regravaram `flgForaSla`, `dsCat`, `dsSca`, `dsTar` e `SlaReal`, e uma rotina de manutenção executada à mão regrava `SlaReal`. A encerrada sem linha em `ReqTimeConcluida` só recebe essa linha quando alguém executa essa rotina, que completa os tempos faltantes e que o produto não agenda nem chama; a linha entra com `dtCalc` igual a `dtFimReal`, de modo que um filtro de `dtCalc` posterior à última carga deixa essa linha de fora.

`RequisicaoLog` também não serve de marca de alteração. Ela data com `dtLog` a mudança de 21 colunas de `Req` (`dsTitulo`, `dsReq`, `nPrioridade`, `idFrmStatus`, `idAre`, `idTar`, `dtAbertura`, `dtIniPrev`, `dtFimPrev`, `dtIniReal`, `dtFimReal`, `sla`, `idGru`, `idGruAtual`, `idFrmOrigem`, `idLoc`, `dsLoc`, `idPat`, `idHie`, `idEmp`, `flgForaSla`), gravada a cada atualização da linha de `Req` em que o valor muda, e algumas inclusões e exclusões de documento e de participante. As outras colunas de `Req`, como `dtResposta`, `dtUltHistADO`, `idFlu`, `flgVinc` e `flgDepende`, ficam fora dela, assim como `ReqConcluida`, as tabelas de tempo e `ReqStatus`.

Por isso, traga `Req`, `ReqTime`, `ReqTimeAdo` e `ReqStatus` inteiras a cada carga, traga as encerradas novas pela regra R-abertas-e-encerradas-02 e refaça de tempos em tempos a carga completa de `ReqConcluida`, `ReqTimeConcluida`, `ReqTimeAdoConcluida` e `ReqStatusConcluida` para captar as alterações posteriores ao encerramento.
Receita: [tempo total por requisição](../receitas/tempo-total-por-requisicao.md)

#### R-abertas-e-encerradas-02: Trate o encerramento como definitivo, leia `Req` antes de `ReqConcluida` e identifique as encerradas novas pelas `idReq` de `ReqConcluida` que ainda faltam no destino. {#r-abertas-e-encerradas-02}
A única inclusão em `Req` é a abertura, que não informa `idReq`: a coluna é `IDENTITY`, e cada abertura recebe um número novo. Nenhum comando apaga linhas de `ReqConcluida`, e a única exclusão de `Req` é a do encerramento, logo depois da cópia. Assim, uma `idReq` passa de `Req` para `ReqConcluida` uma única vez e fica lá: a requisição encerrada não é reaberta.

O encerramento grava `dtFimReal`, recalcula os tempos e move a requisição numa só transação. Ainda assim, leituras separadas das duas tabelas, leituras com `NOLOCK` ou cargas independentes de uma réplica podem ver a requisição nas duas tabelas ou em nenhuma. Leia `Req` antes de `ReqConcluida` e deduplique por `idReq`, com a linha de `ReqConcluida` prevalecendo: a requisição que encerra entre as duas leituras aparece nas duas, e a deduplicação a resolve; na ordem inversa, ela fica fora das duas leituras. Outra saída é ler as duas tabelas no mesmo snapshot.

Compare as `idReq` de `ReqConcluida` com as do destino para achar as encerradas novas: `dtFimReal` recebe a data e hora do servidor de banco no encerramento ou uma data informada no encerramento, que pode ser anterior à última carga.
Receita: [volume por mês](../receitas/volume-por-mes.md)

#### R-abertas-e-encerradas-03: Carregue as encerradas dos demais pares pelas `idReq` das encerradas novas e reconcilie só `ReqPartConcluida`, `ReqDocConcluida` e os apontamentos de requisições em fluxo. {#r-abertas-e-encerradas-03}
Vale para os pares da seção 3 fora das oito tabelas da R-abertas-e-encerradas-01. Nenhum comando do produto apaga linhas das encerradas desses pares, e só o encerramento inclui linhas nelas; a exceção são os apontamentos de uma requisição em fluxo, que entram em `ReqApontConcluida` e `ReqApontAprovConcluida` no encerramento da requisição raiz (seção 3.1). Depois do encerramento, mudam só `ReqPartConcluida.dtUltimoAcesso`, regravada com a hora do servidor de banco quando o usuário abre a requisição encerrada, e `ReqDocConcluida.flgExcluido`, que passa a 1 quando a exclusão de documentos expirados apaga o arquivo vencido em `dtExpiracao`.

Essas encerradas não têm `rowversion` nem data de entrada da linha. As datas delas são do evento: `dtIniReqHist`, `dtFimReqHist` e `dtRegistro` no histórico, `dtInicio` e `dtFim` na participação e nos acessos, `dtEnvioMsg`, `dtInclusao`, `dtDespesa`, `dtGravacao`, `dtAprovacao`, `dtRecat`, `dtKB` e `dtUltHist`. A chave é a da aberta (`idReqHist`, `idReqPart`, `idReqMsg`, `idDoc`, `idReqDesp`, `idReqApont`, `idReqAprov`, `idReqMinutaHist`; nos acessos, o item, `idReqPart` e `dtInicio`; `idReq` em `ReqUltHistConcluida`, `ReqProblemaConcluida` e `ReqMinutaConcluida`; `idReq` e `idKB` em `ReqKBConcluida`), menos em `ReqRecatConcluida`, que recebe `idReqRecat` novo no encerramento, e em `ReqPartRepConcluida`, que não tem chave primária.

Por isso, traga essas encerradas só por acréscimo, pelas `idReq` das encerradas novas (R-abertas-e-encerradas-02), sem filtro de data. As tabelas de acesso e `ReqApontAprovConcluida` não têm `idReq`: a carga delas passa pelas linhas novas da tabela pai (histórico, mensagem, documento ou apontamento), pela chave do item. Em `ReqApontConcluida` e `ReqApontAprovConcluida`, traga as `idReqApont` que faltam no destino. Em `ReqPartConcluida` e `ReqDocConcluida`, atualize `dtUltimoAcesso` e `flgExcluido` por `idReqPart` e `idDoc` nas cargas completas periódicas, ou deixe essas colunas fora. Ligue `ReqRecatConcluida` à requisição por `idReq` e ao histórico por `idReqHist`: o `idReqRecat` dela difere do da aberta. As abertas desses pares perdem as linhas no encerramento, salvo os apontamentos em fluxo: recarregue-as por inteiro.
Receita: [participantes vigentes](../receitas/participantes-vigentes.md)

## Veja também

- [Papéis e participação](papeis-e-participacao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Receita: volume por mês](../receitas/volume-por-mes.md)
- [Modelo](modelo.md)
