# O modelo em 5 minutos

Esta página resume o que você precisa saber antes de escrever a primeira consulta. Cada ponto leva à regra ou à página que o detalha.

## A requisição é o fato central

Tudo gira em volta da requisição (o chamado, na tela do produto). Os outros fatos se ligam a ela pela coluna `idReq`: marcos de prazo, tempos, passagens por status, eventos do histórico, participação, vínculos e avaliação. Os dados adicionais se ligam por `idQQ` ([R-dados-adicionais-01](../fatos/dados-adicionais.md#r-dados-adicionais-01)). O diagrama completo está em [Modelo: a requisição no centro](../mapa/modelo.md).

## Abertas e encerradas ficam em tabelas separadas

- `Req` guarda as requisições abertas e `ReqConcluida` guarda as encerradas. A mesma `idReq` está em uma só das duas, e qualquer volume histórico soma as duas ([R-requisicao-01](../fatos/requisicao.md#r-requisicao-01)).
- O estado (aberta ou encerrada) é a tabela em que a linha está, e não o status. A requisição passa para `ReqConcluida` quando uma transição a leva a um status sem saída ([R-requisicao-06](../fatos/requisicao.md#r-requisicao-06) e [R-status-fase-05](../dimensoes/status-fase.md#r-status-fase-05)).
- A passagem é definitiva: a requisição encerrada não é reaberta ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)).
- Cancelada é um status, de código `CL`, e não uma tabela: a cancelada está em `Req` ou em `ReqConcluida` ([R-status-fase-04](../dimensoes/status-fase.md#r-status-fase-04)).
- A maioria dos fatos repete esse par, como `ReqTime` e `ReqTimeConcluida` ([R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01)). A lista completa está em [Abertas e encerradas](../mapa/abertas-e-encerradas.md).
- A encerrada guarda nomes e classificação como estavam no encerramento, por exemplo a categoria e o nome do grupo ([R-requisicao-03](../fatos/requisicao.md#r-requisicao-03) e [R-grupo-area-03](../dimensoes/grupo-area.md#r-grupo-area-03)).

## Fatos e dimensões

Os **fatos** são o que você conta ou mede. Cada página de fato diz a granularidade, as tabelas da aberta e da encerrada, as colunas-chave e as regras de uso:

| Fato | Uma linha por |
|---|---|
| [Requisição](../fatos/requisicao.md) | requisição |
| [Marcos](../fatos/marcos.md) | requisição (as datas de abertura, prazo, resposta e encerramento) |
| [Tempo da requisição](../fatos/tempo-requisicao.md) | requisição, com os tempos gravados no último cálculo |
| [Tempo por grupo](../fatos/tempo-por-grupo.md) | requisição × participação de quem atendeu |
| [Tempo por status](../fatos/tempo-por-status.md) | passagem da requisição por um status |
| [Eventos do histórico](../fatos/eventos-historico.md) | evento registrado na requisição |
| [Participação](../fatos/participacao.md) | entidade num papel da requisição |

As **dimensões** dão o recorte: [calendário](../dimensoes/tempo-calendario.md), [classificação](../dimensoes/classificacao.md), [status](../dimensoes/status-fase.md), [grupo e área](../dimensoes/grupo-area.md), [pessoa e organização](../dimensoes/pessoa-organizacao.md), [prioridade e SLA](../dimensoes/prioridade-sla.md), [canal e origem](../dimensoes/canal-origem.md) e [ação](../dimensoes/acao.md). A [matriz fato × dimensão](../mapa/matriz-fato-dimensao.md) diz por qual coluna cada cruzamento acontece.

## Os tempos são gravados

Os tempos da requisição não são calculados na hora da consulta: eles ficam gravados com o momento do último cálculo, na coluna `dtCalc` ([R-tempo-requisicao-06](../fatos/tempo-requisicao.md#r-tempo-requisicao-06)). Uma aberta mostra o tempo daquele cálculo, não o de agora. As colunas terminadas em `Cal` estão em minutos do calendário do grupo, e as demais em minutos corridos ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)).

## Código × rótulo

Filtre e agrupe pelo **código**, nunca pelo texto exibido. O texto muda por formulário e por instalação; o código é o que o produto entende.

- Status: o código é `Status.cdSta`, alcançado por `FormStatus.idSta` ([R-status-fase-01](../dimensoes/status-fase.md#r-status-fase-01)).
- Ação do histórico: o código é `Acao.cdAcao` ([R-acao-01](../dimensoes/acao.md#r-acao-01)), e o texto exibido fica em `FormAcao.dsAcao` ([R-acao-02](../dimensoes/acao.md#r-acao-02)).
- Papel do participante: o código é `Papel.cdPapel` ([R-participacao-01](../fatos/participacao.md#r-participacao-01)), e o rótulo no formulário fica em `FormPapel.dsPapel` ([R-participacao-05](../fatos/participacao.md#r-participacao-05)).

Os códigos que o produto define, com o rótulo de cada um, estão em [Valores definidos pelo produto](../dominios-do-produto.md).

## Selos do dicionário

Cada tabela e view do [dicionário de dados](../dicionario/index.md) traz um selo:

- **Explicada:** uma página de fato, de dimensão ou do modelo descreve o significado dela.
- **Citada:** ela aparece em receitas ou páginas de referência, mas não tem página de negócio própria.
- **Só estrutura:** a página traz só as colunas e os tipos. Não deduza o significado pelo nome da coluna.

## "Em revisão" e "decisão do produto"

- **Em revisão:** a receita com esse aviso ainda não teve a definição verificada por completo. Use-a com cautela e confira os resultados. O mesmo rótulo ao lado do título de uma regra indica uma regra ainda em revisão.
- **Decisão do produto:** marca uma definição escolhida pelo produto quando o banco permite mais de uma leitura, por exemplo o que conta como primeira resposta ([R-marcos-01](../fatos/marcos.md#r-marcos-01)) ou como prazo estourado ([R-marcos-02](../fatos/marcos.md#r-marcos-02)). Use essa definição para que o seu número bata com o do produto.

## Próximo passo

Leia as [regras de ouro](regras-de-ouro.md) e, em seguida, a receita mais próxima do seu indicador.
