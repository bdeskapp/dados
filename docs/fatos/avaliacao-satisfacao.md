---
gerado: sincronizacao
---
# Fato: avaliação e satisfação


## 1. O que mede

Dois registros distintos de satisfação com o atendimento:

- a **avaliação da requisição** (`ReqAvaliacao`): uma nota simples e um comentário opcional, dados quando a requisição é avaliada ou encerrada;
- a **pesquisa de satisfação** (`Pesquisa` e `Pesq*`): um questionário configurável (perguntas e opções com peso) respondido a respeito de uma requisição.

## 2. Granularidade

- `ReqAvaliacao`: uma linha por requisição (`idReq` é a chave). Uma requisição tem no máximo uma linha, e ela pode existir sem nota (`opAvaliacao` vazio).
- `PesqRespCab`: uma linha por resposta a uma pesquisa (`idResp`). Uma requisição pode ter mais de uma resposta, inclusive à mesma pesquisa, quando as respostas vêm de usuários diferentes, quando a pesquisa é anônima, porque nela o produto não confere a resposta repetida por usuário, ou quando a pesquisa permite responder mais de uma vez (`Pesquisa.flgResponderMaisDeUmaVez`).
- `PesqResposta`: uma linha por pergunta respondida (`idResp`, `idPergunta`).

## 3. Tabelas

| Tabela | Conteúdo | Observação |
|---|---|---|
| `ReqAvaliacao` | nota (`opAvaliacao`), comentário (`dsAvaliacao`) e autor (`idUsu`) | uma só tabela para abertas e encerradas |
| `Pesquisa` | definição da pesquisa (título, vigência, anônima, grupo dono) | |
| `PesqPergunta` | perguntas da pesquisa (`idPesq`) | |
| `PesqOpcao` | opções de resposta, com `nPeso` | |
| `PesqRespCab` | cabeçalho da resposta: pesquisa, data, usuário, requisição (`idReq`) | uma só tabela para abertas e encerradas |
| `PesqResposta` | resposta a cada pergunta: opção escolhida (`idOpc`) ou texto (`dsResposta`) | |

- **Quem grava `ReqAvaliacao`.** O produto, em duas situações: no encerramento, quando a requisição ainda não tem avaliação, e na ação `AVAL`, que grava a nota da requisição sem conferir se ela está encerrada: a validação confere só se o usuário pode executar a ação no status atual da requisição, aberta ou encerrada; por isso `ReqAvaliacao` também tem avaliação de requisição aberta. O autor (`idUsu`) é o usuário que executou a ação; no encerramento sem usuário identificado, o produto grava o usuário de código 1.
- **Quem grava a pesquisa.** A cada resposta, o produto insere `PesqRespCab` e uma linha de `PesqResposta` por pergunta respondida. Quando a pesquisa é geral, conforme `tpPesquisa`, a resposta não leva requisição (`idReq`, `idFrm` e `idProc` vazios); nas demais, `idReq`, `idFrm` e `idProc` identificam a requisição.
- **Sem par aberta/encerrada.** `ReqAvaliacao` e `PesqRespCab` mantêm a linha onde está quando a requisição é encerrada; liga-se a `Req` ou a `ReqConcluida` por `idReq`.

## 4. Colunas-chave

| Coluna | Significado | Unidade |
|---|---|---|
| `ReqAvaliacao.idReq` | requisição avaliada | |
| `ReqAvaliacao.opAvaliacao` | nota da avaliação, em código numérico gravado pelo produto; vazio quando a avaliação foi registrada sem nota | código |
| `ReqAvaliacao.dsAvaliacao` | comentário | texto |
| `ReqAvaliacao.idUsu` | usuário que registrou a avaliação | |
| `PesqRespCab.idResp` | identificador da resposta | |
| `PesqRespCab.idPesq` | pesquisa respondida | |
| `PesqRespCab.idReq` | requisição a que a resposta se refere | |
| `PesqRespCab.dtResp` | momento da resposta | data e hora |
| `PesqRespCab.idUsu` | quem respondeu; vazio quando a pesquisa é anônima | |
| `PesqResposta.idOpc` | opção escolhida (`PesqOpcao`; `nPeso` é o peso) | |
| `PesqResposta.flgAbstencao` | pergunta respondida como abstenção | |

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Grupo | pelo grupo atual da requisição: `Req.idGruAtual` ou `ReqConcluida.idGruAtual` → `Grupo.idGru` |
| Usuário | `ReqAvaliacao.idUsu` / `PesqRespCab.idUsu` → `Usuario.idUsu` |
| Pesquisa | `PesqRespCab.idPesq` → `Pesquisa.idPesq`; `PesqResposta.idResp` → `PesqRespCab.idResp` |

## 6. Regras de uso

#### R-avaliacao-satisfacao-01: Calcule satisfação só sobre as requisições avaliadas, isto é, com `opAvaliacao` preenchido. {#r-avaliacao-satisfacao-01}
Uma linha de `ReqAvaliacao` pode existir sem nota. A distribuição por nota usa as linhas com `opAvaliacao IS NOT NULL`.
Receita: [avaliações por grupo](../receitas/avaliacoes-por-grupo.md)

#### R-avaliacao-satisfacao-02: Apresente a taxa de resposta à parte: avaliadas dividido pelas encerradas do recorte. {#r-avaliacao-satisfacao-02}
As encerradas sem avaliação entram só no denominador da taxa; ficam fora da distribuição por nota. Como `ReqAvaliacao` também guarda avaliação de requisição ainda aberta (a ação `AVAL` não confere o encerramento), parta de `ReqConcluida` com `LEFT JOIN ReqAvaliacao`: o numerador são as encerradas avaliadas. A taxa de resposta tem dois denominadores, que a receita apresenta lado a lado: as encerradas do recorte sem as canceladas (status de código `CL`), que responde "das atendidas e encerradas, quantas foram avaliadas", e as encerradas com linha em `ReqAvaliacao`, com ou sem nota, que responde "dos registros de avaliação, quantos trazem nota" ([avaliações por grupo](../receitas/avaliacoes-por-grupo.md)).
Receita: [avaliações por grupo](../receitas/avaliacoes-por-grupo.md)

#### R-avaliacao-satisfacao-03: Leia `opAvaliacao` como código e apresente a distribuição por código. {#r-avaliacao-satisfacao-03}
A escala tem sentido definido pelo produto, mas o texto de cada nota não está em [Valores definidos pelo produto](../dominios-do-produto.md); por isso as receitas devolvem a contagem por código, por grupo, sem média.
Receita: [avaliações por grupo](../receitas/avaliacoes-por-grupo.md)

#### R-avaliacao-satisfacao-04: Ligue a pesquisa à requisição por `PesqRespCab.idReq`. {#r-avaliacao-satisfacao-04}
`Pesquisa` descreve o questionário, `PesqRespCab` a resposta e `PesqResposta` cada pergunta respondida. A resposta serve a abertas e encerradas.

## 7. Views recomendadas

Nenhuma. `ReqAvaliacao` e `PesqRespCab` respondem direto às perguntas desta página.

## 8. Receitas

- [Avaliações por grupo](../receitas/avaliacoes-por-grupo.md)

## Veja também

- [Fato: requisição](requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
