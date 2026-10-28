---
gerado: sincronizacao
---
# Views recomendadas


Esta página reúne as views que as páginas de fatos, dimensões e mapa recomendam. Para cada uma: a pergunta que responde, a granularidade, o que cobre e como usar. O texto vem da página que a recomenda, que é a referência. Para qualquer outra pergunta, a documentação recomenda as tabelas.

## `vwReq` e `vwReqTotal`

- **Pergunta que respondem:** lista e volume de requisições, abertas e encerradas, numa só consulta.
- **Granularidade:** uma linha por requisição.
- **Cobre:** abertas e encerradas (`UNION ALL` de `Req` e `ReqConcluida`).
- **Como usar:** escolha `vwReq` quando a descrição não é necessária; `vwReqTotal` acrescenta a coluna `dsReq` (descrição completa). A coluna `ReqStatus` informa a tabela de origem (`Aberta` ou `Encerrada`) e é outro objeto, distinto da tabela `ReqStatus`. Em `dsSta`, a linha aberta mostra o rótulo atual do status e a encerrada mostra o rótulo gravado no encerramento; para a leitura pelo código, junte `FormStatus` e `Status`. Aplicam `LEFT JOIN` em `FormStatus` e não filtram linhas: a soma de linhas das duas views é igual à soma de `Req` e `ReqConcluida`. As views trazem `dtAbertura`, `dtIniPrev`, `dtFimPrev`, `dtIniReal` e `dtFimReal`; `dtResposta`, `dtUltHistADO`, `flgForaSLA` e `SLAOrig` não fazem parte delas, e as páginas de fato recomendam lê-las em `Req` ∪ `ReqConcluida`.
- **Página que recomenda:** [Fato: requisição](../fatos/requisicao.md), [Abertas e encerradas](../mapa/abertas-e-encerradas.md), [Marcos](../fatos/marcos.md) (colunas de data) e [Status e fase](../dimensoes/status-fase.md).

## `vwRepUltimaAcao`

- **Pergunta que responde:** qual foi a última ação de cada requisição.
- **Granularidade:** uma linha por requisição que tenha linha em `ReqUltHist` ou `ReqUltHistConcluida`.
- **Cobre:** abertas e encerradas (`UNION ALL` de `ReqUltHist` e `ReqUltHistConcluida`, sem filtro).
- **Como usar:** traz `Quem` (nome do autor, ou "Execução Automática" quando `idUsu` é vazio ou não existe em `Usuario`), `Ação`, `dtAcao` e `Motivo`. A ação vem do rótulo gravado (`dsAcao`); para o código da ação, ligue `idFrmAcao` a `FormAcao` e `Acao`. Para o histórico completo, a recomendação são as tabelas `ReqHistorico` e `ReqHistConcluida`.
- **Página que recomenda:** [Fato: eventos do histórico](../fatos/eventos-historico.md).

## `vwRepTimeStatus`

- **Pergunta que responde:** tempo em minutos de calendário por passagem de status.
- **Granularidade:** uma linha por passagem de status.
- **Cobre:** abertas e encerradas, com `idReq`, `idFrmStatus`, `tStatusCal` (= `nIntervaloCal`) e `dtFimStatus`.
- **Como usar:** junte `idFrmStatus` a `FormStatus` e `Status` para chegar ao código; para minutos corridos ou para `dtIniStatus`, use as tabelas da página do fato.
- **Página que recomenda:** [Fato: tempo por status](../fatos/tempo-por-status.md).

## `vwReqAcessoTotal`, `vwReqAcesso` e `vwReqAcessoConcluida`

- **Pergunta que respondem:** quais usuários têm acesso a uma requisição, ou quais requisições um usuário pode ver.
- **Granularidade:** uma linha por requisição × participante com acesso × usuário. Um grupo participante gera uma linha para cada membro; `flgGrupo = 1` marca também os membros de Hierarquia e de Grupo de Acesso. O mesmo usuário aparece em mais de uma linha da mesma requisição quando participa por mais de um caminho; para listar requisições use `COUNT(DISTINCT idReq)` ou `SELECT DISTINCT idReq`.
- **Cobre:** `vwReqAcessoTotal` cobre abertas e encerradas (`UNION ALL` de `vwReqAcesso` e `vwReqAcessoConcluida`); `vwReqAcesso` cobre só abertas e `vwReqAcessoConcluida` só encerradas, com a mesma granularidade.
- **Como usar:** filtre sempre por `idUsu` ou por `idReq`. As views dão acesso por participação: entram só participações vigentes (`dtFim` vazia, coluna que não aparece no resultado), de papéis com `FormPapel.flgAcesso = 1` (`vwReqAcesso`), nos tipos de participante Usuário, Gestor, Contato, Grupo, Grupo de Acesso e Hierarquia (`vwReqAcessoInterna`). Uma subconsulta retira a linha do usuário que tem, na mesma requisição, participação em papel com `flgAcesso = 0` dos tipos `1`, `8`, `7` ou `13`; ela não filtra `dtFim` (conta também participações encerradas) e, nos tipos `7` e `13`, compara `idPart`, que não é id de usuário, com `idUsu`. A regra completa está no complemento de [Papéis e participação](../mapa/papeis-e-participacao.md), seção 5. As views `vwUsuPartQpoqq*` levam a sigla `QPOQQ`, que significa "Quem Pode O Que Quando" (decisão do produto).
- **Páginas que recomendam:** [Fato: participação](../fatos/participacao.md) e [Papéis e participação](../mapa/papeis-e-participacao.md), seção 5.

## `vwReqApontTotal`, `vwReqApontAprovTotal` e `vwReqDespTotal`

- **Pergunta que respondem:** horas apontadas, decisões sobre os apontamentos e despesas de uma requisição, abertas e encerradas, numa só consulta.
- **Granularidade:** `vwReqApontTotal`, uma linha por apontamento (`idReqApont`); `vwReqApontAprovTotal`, uma linha por decisão (`idReqApont`); `vwReqDespTotal`, uma linha por despesa (`idReqDesp`).
- **Cobre:** abertas e encerradas (`UNION ALL` de `ReqApontamento` e `ReqApontConcluida`; de `ReqApontAprov` e `ReqApontAprovConcluida`; de `ReqDespesa` e `ReqDespConcluida`), sem filtro: a contagem de cada view é a soma das duas tabelas. Um mesmo `idReqApont` ou `idReqDesp` fica em um lado só, porque o encerramento da requisição e o do fluxo copiam para a tabela de encerradas e em seguida apagam da aberta.
- **Como usar:** `vwReqApontTotal` tem as colunas das tabelas e nenhuma coluna de origem; `vwReqApontAprovTotal` não tem `idReq`: junte-a a `vwReqApontTotal` por `idReqApont` (`LEFT JOIN` para manter o apontamento sem decisão) e acrescenta `nmUsuAprov`; `vwReqDespTotal` traz `ReqStatus` (`Aberta` ou `Encerrada`, outro objeto que a tabela `ReqStatus`), os rótulos `nmUsu`, `dsCatDesp`, `dsItemDesp` e o fornecedor em `nmFornecedor`. O produto usa `vwReqApontTotal` no relatório de apontamentos e na soma de horas apontadas por período, `vwReqApontAprovTotal` no faturamento e `vwReqDespTotal` na leitura das despesas. A despesa que o encerramento não copiou não está em nenhum dos lados ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).
- **Página que recomenda:** [Fato: apontamento e despesas](../fatos/apontamento-e-despesas.md).

## Veja também

- [Modelo](../mapa/modelo.md)
- [Matriz fato × dimensão](../mapa/matriz-fato-dimensao.md)
- [INDEX](../busca.md)
