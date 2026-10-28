---
gerado: sincronizacao
---
# Regras essenciais


Uma linha por regra `R-…` das páginas de fatos e do mapa, agrupadas por página, com o título da regra e o link para a âncora. A explicação de cada regra e a receita que a aplica estão na página dona. Total: 70 regras, 67 dos fatos e 3 do mapa. A seção [Mapa](#mapa) traz as 3 regras de extração da página [Abertas e encerradas](abertas-e-encerradas.md). As regras das dimensões estão em [regras essenciais das dimensões](regras-essenciais-dimensoes.md) (41 regras).

## Fato: requisição

Página: [Fato: requisição](../fatos/requisicao.md)

- [R-requisicao-01](../fatos/requisicao.md#r-requisicao-01): Some abertas e encerradas para qualquer volume histórico.
- [R-requisicao-02](../fatos/requisicao.md#r-requisicao-02): Leia o estado (aberta ou encerrada) pela tabela de origem, e o status pelo código `Status.cdSta`.
- [R-requisicao-03](../fatos/requisicao.md#r-requisicao-03): Leia a classificação de uma encerrada nas colunas de retrato de `ReqConcluida`, e a de uma aberta em `Tarefa`.
- [R-requisicao-04](../fatos/requisicao.md#r-requisicao-04): Use `LEFT JOIN` ao ligar `Req.idTar` a `Tarefa`.
- [R-requisicao-05](../fatos/requisicao.md#r-requisicao-05): Leia o grupo atual em `idGruAtual` e o nome em `Grupo.dsGru`.
- [R-requisicao-06](../fatos/requisicao.md#r-requisicao-06): Leia o estado da requisição pela tabela em que ela está; a mudança de tabela acontece quando uma transição leva ao status terminal.

## Fato: marcos da requisição

Página: [Fato: marcos da requisição](../fatos/marcos.md)

- [R-marcos-01](../fatos/marcos.md#r-marcos-01): Leia a primeira resposta em `dtResposta`.
- [R-marcos-02](../fatos/marcos.md#r-marcos-02): Compare `dtFimPrev` com `dtFimReal` nas encerradas e com o momento da consulta nas abertas para saber se estourou o prazo.
- [R-marcos-03](../fatos/marcos.md#r-marcos-03): Leia o encerramento em `dtFimReal`, que só existe nas encerradas.
- [R-marcos-04](../fatos/marcos.md#r-marcos-04): Leia o prazo pelas datas; `flgForaSLA` é gravada pelo plano de alertas e regravada com 0 por uma atualização de versão do produto.
- [R-marcos-05](../fatos/marcos.md#r-marcos-05): Leia o início real em `dtIniReal` e a primeira resposta em `dtResposta` como marcos diferentes.
- [R-marcos-06](../fatos/marcos.md#r-marcos-06): Leia as datas como hora local dos servidores da instalação, sem fuso gravado.
- [R-marcos-07](../fatos/marcos.md#r-marcos-07): Nas abertas, leia o "agora" uma vez por carga e grave-o junto com o resultado.

## Fato: tempo da requisição

Página: [Fato: tempo da requisição](../fatos/tempo-requisicao.md)

- [R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01): Some `ReqTime` e `ReqTimeConcluida` para qualquer tempo histórico.
- [R-tempo-requisicao-02](../fatos/tempo-requisicao.md#r-tempo-requisicao-02): Parta de `Req` com `LEFT JOIN ReqTime` quando a lista precisa conter todas as abertas.
- [R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03): Leia os campos `...Cal` em minutos do calendário do grupo e os campos sem sufixo em minutos corridos.
- [R-tempo-requisicao-04](../fatos/tempo-requisicao.md#r-tempo-requisicao-04): Leia o tempo total em `tTotalCal` e o desmembramento ativo e congelado do atendimento em `ReqTimeAdo`.
- [R-tempo-requisicao-05](../fatos/tempo-requisicao.md#r-tempo-requisicao-05): Leia o tempo até a primeira resposta em `tRespCal` e mantenha só as requisições com `dtResposta` preenchida.
- [R-tempo-requisicao-06](../fatos/tempo-requisicao.md#r-tempo-requisicao-06): Leia a atualidade do tempo em `dtCalc`.
- [R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07): Grave `dtCalc` junto com os tempos de cada aberta e meça a defasagem como a diferença entre o horário da carga e `dtCalc`.
- [R-tempo-requisicao-08](../fatos/tempo-requisicao.md#r-tempo-requisicao-08): Reproduza os minutos de calendário intervalo a intervalo, truncando ao minuto o início e o fim de cada um e contando os minutos de relógio que caem nas faixas do calendário.
- [R-tempo-requisicao-09](../fatos/tempo-requisicao.md#r-tempo-requisicao-09): Conte que `tTotal`, `tAtivo` e `tFreeze` perdem minutos quando o relógio do produto está adiantado em relação ao do banco.

## Fato: tempo de atendimento por grupo

Página: [Fato: tempo de atendimento por grupo](../fatos/tempo-por-grupo.md)

- [R-tempo-por-grupo-01](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-01): Leia o grupo em `ReqParticipante.idPart` quando `idTpPapel = 2`.
- [R-tempo-por-grupo-02](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-02): Some `ReqTimeAdo` e `ReqTimeAdoConcluida` para qualquer histórico.
- [R-tempo-por-grupo-03](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-03): Leia o tempo por grupo em `ReqTimeAdo`, cujo grão é requisição × participação (`idReqPart`).
- [R-tempo-por-grupo-04](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-04): Junte a linha de tempo à participação por `idReqPart` e confirme `ReqParticipante.idReq = ReqTimeAdo.idReq`.
- [R-tempo-por-grupo-05](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-05): Entenda o tempo de atendimento como o tempo posterior à primeira resposta.

## Fato: tempo por status

Página: [Fato: tempo por status](../fatos/tempo-por-status.md)

- [R-tempo-por-status-01](../fatos/tempo-por-status.md#r-tempo-por-status-01): Some `ReqStatus` e `ReqStatusConcluida` para qualquer histórico.
- [R-tempo-por-status-02](../fatos/tempo-por-status.md#r-tempo-por-status-02): Conte passagens por linha e requisições por `COUNT(DISTINCT idReq)`.
- [R-tempo-por-status-03](../fatos/tempo-por-status.md#r-tempo-por-status-03): Leia o status pelo código, por `FormStatus.idSta` → `Status.cdSta`.
- [R-tempo-por-status-04](../fatos/tempo-por-status.md#r-tempo-por-status-04): Entenda a passagem atual de uma aberta como uma passagem em curso.

## Fato: eventos do histórico

Página: [Fato: eventos do histórico](../fatos/eventos-historico.md)

- [R-eventos-historico-01](../fatos/eventos-historico.md#r-eventos-historico-01): Leia o código da ação por `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- [R-eventos-historico-02](../fatos/eventos-historico.md#r-eventos-historico-02): Leia o autor do evento em `idUsu`; `idReqPart` é a participação sob a qual o evento foi registrado.
- [R-eventos-historico-03](../fatos/eventos-historico.md#r-eventos-historico-03): Leia a data do evento em `dtFimReqHist`.
- [R-eventos-historico-04](../fatos/eventos-historico.md#r-eventos-historico-04): Conte direcionamentos pelas ações `DIR` e rejeições de conclusão pelas ações `REJCON`.
- [R-eventos-historico-05](../fatos/eventos-historico.md#r-eventos-historico-05): O último evento registrado de uma encerrada é o de maior `idReqHist`, que é o evento de `ReqUltHistConcluida`.
- [R-eventos-historico-06](../fatos/eventos-historico.md#r-eventos-historico-06): Leia "última ação" de uma requisição em `ReqUltHist` (abertas) e `ReqUltHistConcluida` (encerradas).

## Fato: participação

Página: [Fato: participação](../fatos/participacao.md)

- [R-participacao-01](../fatos/participacao.md#r-participacao-01): Leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- [R-participacao-02](../fatos/participacao.md#r-participacao-02): Filtre o participante vigente com `dtFim IS NULL`.
- [R-participacao-03](../fatos/participacao.md#r-participacao-03): Leia `idPart` conforme o tipo.
- [R-participacao-04](../fatos/participacao.md#r-participacao-04): Leia o nome exibido em `PartTipoPapel.nmPart`, por `LEFT JOIN` no par (`idTpPapel`, `idPart`).
- [R-participacao-05](../fatos/participacao.md#r-participacao-05): Leia o rótulo do papel em `FormPapel.dsPapel` quando a pergunta é "como o formulário chama este papel".
- [R-participacao-06](../fatos/participacao.md#r-participacao-06): Conte participações por `idReqPart` e requisições por `COUNT(DISTINCT idReq)`.

## Fato: dados adicionais

Página: [Fato: dados adicionais](../fatos/dados-adicionais.md)

- [R-dados-adicionais-01](../fatos/dados-adicionais.md#r-dados-adicionais-01): Ligue `DadValor` à requisição por `idQQ` e filtre `DadContextoCampo.idEnt = 3`.
- [R-dados-adicionais-02](../fatos/dados-adicionais.md#r-dados-adicionais-02): Leia abertas e encerradas na mesma `DadValor`, juntando com `Req` e com `ReqConcluida`.
- [R-dados-adicionais-03](../fatos/dados-adicionais.md#r-dados-adicionais-03): Chegue ao campo por `DadValor.idDadCon → DadContextoCampo.idDad → DadoAdicional`.
- [R-dados-adicionais-04](../fatos/dados-adicionais.md#r-dados-adicionais-04): Leia o valor na coluna que o `tpDado` indica.
- [R-dados-adicionais-05](../fatos/dados-adicionais.md#r-dados-adicionais-05): Para campo de lista, leia os itens em `DadValorDominio`, o rótulo em `DadDominio.dsDom`, e conte requisições com `COUNT(DISTINCT idQQ)`.
- [R-dados-adicionais-06](../fatos/dados-adicionais.md#r-dados-adicionais-06): Os valores gravados permanecem depois que o contexto é desativado.
- [R-dados-adicionais-07](../fatos/dados-adicionais.md#r-dados-adicionais-07): Use `flgAgenda = 0` para o valor de requisição.
- [R-dados-adicionais-08](../fatos/dados-adicionais.md#r-dados-adicionais-08): Trate `nSeq` como parte da chave do valor.
- [R-dados-adicionais-09](../fatos/dados-adicionais.md#r-dados-adicionais-09): No pivô, confira a contagem de contextos de cada campo.
- [R-dados-adicionais-10](../fatos/dados-adicionais.md#r-dados-adicionais-10): Para os formulários de um campo, combine o escopo do contexto com o formulário das requisições que têm valor.

## Fato: vínculos entre requisições

Página: [Fato: vínculos entre requisições](../fatos/vinculos.md)

- [R-vinculos-01](../fatos/vinculos.md#r-vinculos-01): Ache as filhas de um pai em `ReqVinculada` (`idReq` = pai) e em `ReqVinculadaRef` com `cdVinc` `DESDD` (`idReqVinculo` = pai).
- [R-vinculos-02](../fatos/vinculos.md#r-vinculos-02): Resolva o estado de pai e filha com `LEFT JOIN` em `Req` e em `ReqConcluida`.
- [R-vinculos-03](../fatos/vinculos.md#r-vinculos-03): Leia o código do vínculo com `RTRIM(cdVinc)`, e o tipo em `idTpVinculo`.
- [R-vinculos-04](../fatos/vinculos.md#r-vinculos-04): Leia o sentido de `ReqVinculadaRef` pelo código do vínculo.

## Fato: avaliação e satisfação

Página: [Fato: avaliação e satisfação](../fatos/avaliacao-satisfacao.md)

- [R-avaliacao-satisfacao-01](../fatos/avaliacao-satisfacao.md#r-avaliacao-satisfacao-01): Calcule satisfação só sobre as requisições avaliadas, isto é, com `opAvaliacao` preenchido.
- [R-avaliacao-satisfacao-02](../fatos/avaliacao-satisfacao.md#r-avaliacao-satisfacao-02): Apresente a taxa de resposta à parte: avaliadas dividido pelas encerradas do recorte.
- [R-avaliacao-satisfacao-03](../fatos/avaliacao-satisfacao.md#r-avaliacao-satisfacao-03): Leia `opAvaliacao` como código e apresente a distribuição por código.
- [R-avaliacao-satisfacao-04](../fatos/avaliacao-satisfacao.md#r-avaliacao-satisfacao-04): Ligue a pesquisa à requisição por `PesqRespCab.idReq`.

## Fato: apontamento e despesas

Página: [Fato: apontamento de horas e despesas](../fatos/apontamento-e-despesas.md)

- [R-apontamento-e-despesas-01](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-01): Leia `qtdHoras` como minutos e divida por 60 para apresentar horas.
- [R-apontamento-e-despesas-02](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-02): Tome a duração do apontamento em `qtdHoras`.
- [R-apontamento-e-despesas-03](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-03): Ligue a decisão ao apontamento por `ReqApontAprov.idReqApont` com `LEFT JOIN`, leia a rejeição por `tpAprovacao` e compare lançado com decidido só no agregado.
- [R-apontamento-e-despesas-04](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-04): Identifique o apontamento por `idReqApont` e use `idSeq` como grupo de apontamentos da requisição.
- [R-apontamento-e-despesas-05](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-05): Cubra a requisição em qualquer estado pelas views de união, e leia o apontamento de requisição de fluxo na tabela aberta até o encerramento do fluxo.
- [R-apontamento-e-despesas-06](../fatos/apontamento-e-despesas.md#r-apontamento-e-despesas-06): Some `valDespesa` por `idCatDesp` e `idItemDesp`; o gasto da requisição é a soma de `valDespesa`.

## Mapa

Página: [Abertas e encerradas](abertas-e-encerradas.md)

- [R-abertas-e-encerradas-01](abertas-e-encerradas.md#r-abertas-e-encerradas-01): Recarregue as abertas por inteiro a cada carga e reconcilie as encerradas com cargas completas periódicas, porque as oito tabelas da requisição e dos tempos não registram a data de alteração da linha.
- [R-abertas-e-encerradas-02](abertas-e-encerradas.md#r-abertas-e-encerradas-02): Trate o encerramento como definitivo, leia `Req` antes de `ReqConcluida` e identifique as encerradas novas pelas `idReq` de `ReqConcluida` que ainda faltam no destino.
- [R-abertas-e-encerradas-03](abertas-e-encerradas.md#r-abertas-e-encerradas-03): Carregue as encerradas dos demais pares pelas `idReq` das encerradas novas e reconcilie só `ReqPartConcluida`, `ReqDocConcluida` e os apontamentos de requisições em fluxo.

## Veja também

- [Regras essenciais das dimensões](regras-essenciais-dimensoes.md)
- [Modelo](modelo.md)
- [Matriz fato × dimensão](matriz-fato-dimensao.md)
