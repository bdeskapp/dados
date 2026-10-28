---
gerado: sincronizacao
---
# Fato: eventos do histórico


## 1. O que mede

O que aconteceu com a requisição ao longo do tempo: cada ação executada (direcionar, concluir, rejeitar a conclusão, encerrar, cancelar, acompanhar e assim por diante), quem a executou e quando. É a base para contar direcionamentos, rejeições de conclusão e para saber quem levou a requisição ao seu último estado.

## 2. Granularidade

Uma linha por evento. Uma requisição tem vários eventos, e o identificador do evento é `idReqHist`. O produto grava uma linha a cada ação. Os identificadores `idReqHist` da tabela aberta e da encerrada não se repetem: um evento está numa só das duas.

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `ReqHistorico` | |
| Encerrada | `ReqHistConcluida` | acrescenta cópias gravadas no encerramento: `nmPart`, `nmUsu`, `nmPersona`, `dsGru`, `dsAcao`, `dsMotivo`, `dsSta`, `dsTitulo` |
| Última ação, aberta | `ReqUltHist` | uma linha por requisição, com o último evento |
| Última ação, encerrada | `ReqUltHistConcluida` | idem |
| Ação | `FormAcao` → `Acao` | `Acao.cdAcao` é o código da ação ([Valores definidos pelo produto](../dominios-do-produto.md)) |
| Motivo | `FormAcaoMotivo` | `idMotivo` do evento |
| Autor | `Usuario` | por `idUsu` |

- **Quem grava.** A cada ação, o produto insere o evento em `ReqHistorico` e, na sequência, troca a linha de `ReqUltHist` da requisição pelo novo último evento. No encerramento, os eventos passam para `ReqHistConcluida` e `ReqUltHist` para `ReqUltHistConcluida`.
- **Escolha de tabela.** Para volume de eventos use as duas tabelas, `ReqHistorico` e `ReqHistConcluida`, por `UNION ALL`. Para chegar ao código da ação, ligue `idFrmAcao` a `FormAcao` e `FormAcao.idAcao` a `Acao`.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReqHist` | identificador do evento | |
| `idReq` | requisição | |
| `idReqPart` | participação da requisição sob a qual o evento foi registrado | |
| `idUsu` | autor do evento; vazio quando o evento não tem usuário gravado; o evento do sistema é marcado por `flgSYS` (R-eventos-historico-02) | |
| `idFrmAcao` | ação do formulário; leva a `Acao.cdAcao` | |
| `idMotivo` | motivo da ação, quando há | |
| `idFrmStatus` | status do formulário registrado no evento | |
| `dtFimReqHist` | momento do evento; é a data que a tela exibe como "Data" | data e hora |
| `dtIniReqHist` | início do intervalo que o evento fecha: o `dtUltHist` do evento anterior (com ajustes nos primeiros eventos) | data e hora |
| `dtRegistro` | instante em que a linha foi inserida (padrão `getdate()`) | data e hora |
| `idReqPartADO` | participação do solicitado (papel `ADO`) no momento do evento | |
| `dsReqHist` | texto do evento (mensagem, justificativa) | texto |
| `flgPublico` | visibilidade do evento na linha do tempo | |
| `tpRegistro` | classificação do registro, definida pela operação que grava o evento: `A` em diversos registros, `R` na ação `ACO`, `M` para a mensagem, `D` para o documento anexado e `P` no histórico de participante, gravado na exclusão de participante e na inclusão de participante, com a ação `INCPAR`; o produto, ao ler o histórico, trata `R` e `D` pela visibilidade (`flgPublico` ou `ReqHistAcesso`) e `M` pela mensagem | |

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Ação | `idFrmAcao` → `FormAcao.idFrmAcao`; `FormAcao.idAcao` → `Acao.idAcao`; código em `Acao.cdAcao` |
| Autor | `idUsu` → `Usuario.idUsu` |
| Participação | `idReqPart` → `ReqParticipante.idReqPart` ou `ReqPartConcluida.idReqPart` |
| Grupo da requisição | o grupo atual está em `Req.idGruAtual` / `ReqConcluida.idGruAtual`; liga-se ao evento por `idReq` |

## 6. Regras de uso

#### R-eventos-historico-01: Leia o código da ação por `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`. {#r-eventos-historico-01}
`FormAcao.dsAcao` é o rótulo da ação naquele formulário e pode diferir do rótulo do produto; o código `cdAcao` é o mesmo em todos os formulários. `Acao.cdAcao` não é único em `Acao` (um código de ação criado pela instalação, com `flgSistema = 0`, aparece em mais de um registro); o `JOIN` por `idAcao` não multiplica linhas, e as ações das receitas desta página têm um registro cada.
Receita: [mudanças de grupo](../receitas/mudancas-de-grupo.md)

#### R-eventos-historico-02: Leia o autor do evento em `idUsu`; `idReqPart` é a participação sob a qual o evento foi registrado. {#r-eventos-historico-02}
Quando o autor é um usuário que age em nome próprio, a participação é a dele (tipo Usuário, `idPart` igual a `idUsu`); quando age em nome de um grupo, a participação é do tipo Grupo e `idUsu` continua preenchido; quando o evento vem do sistema, ele é marcado com `flgSYS = 1` e registrado sob a participação de tipo Sistema (`11`, [Valores definidos pelo produto](../dominios-do-produto.md)): com `flgSYS = 1`, o produto busca só a participação de tipo `11`; o evento do acompanhamento por e-mail fica sob a participação dominante do remetente identificado; quando a ação pedida no e-mail falha e a configuração do acompanhamento por e-mail permite, o produto registra a ação `EMAIL` sob a participação de tipo E-mail (`14`) de papel `EMAIL`, e reconheça os eventos dessa participação pelo papel `EMAIL`. O produto grava `idUsu` e `flgSYS` como os recebe; na abertura pela integração com o Zabbix, o evento é gravado com `flgSYS = 0` fixo. Então identifique o evento do sistema por `flgSYS` e leia `idUsu`, que pode vir vazio ou preenchido. `Usuario` ligado por `LEFT JOIN` mantém os eventos sem usuário.
Receita: [quem encerrou](../receitas/quem-encerrou.md)

#### R-eventos-historico-03: Leia a data do evento em `dtFimReqHist`. {#r-eventos-historico-03}
É o instante do evento: o produto grava a hora corrente, ou a data informada em registros offline; no primeiro evento da requisição (sem última ação gravada), o registro offline usa a data de início real ou, na falta dela, a prevista, e o registro de requisição agendada, cuja data de início é posterior à hora corrente, usa `dtAbertura`. É também a coluna "Data" do histórico na tela. `dtRegistro` é o instante da inserção da linha e desempata eventos do mesmo `dtFimReqHist`.
Receita: [rejeições de conclusão](../receitas/rejeicoes-de-conclusao.md)

#### R-eventos-historico-04: Conte direcionamentos pelas ações `DIR` e rejeições de conclusão pelas ações `REJCON`. {#r-eventos-historico-04}
Cada evento com `cdAcao` `DIR` é um direcionamento, para um grupo ou para um usuário, e cada evento `REJCON` é uma rejeição da conclusão. O status seguinte vem da transição em `FormTransicao` (`idFrmStatusProx`), e a rejeição pode deixar a requisição encerrada, conforme a transição do formulário (`FormTransicao`): nesse caso o `REJCON` é o último evento de uma requisição de `ReqConcluida` (`ReqUltHistConcluida`). A contagem de `DIR` não inclui as trocas de `idGruAtual` por devolução, por categorização (`CAT`), por recategorização (`RECAT`) nem pela transição que define grupo solucionador: a troca de grupo solucionador grava o grupo de `FormTransGrupoSolucionador` para o status e a ação do evento, qualquer que seja a ação, apenas quando há participante `ADO` vigente; o evento de abertura pela integração com o Zabbix não a aplica. Some `ReqHistorico` e `ReqHistConcluida`.
Receita: [mudanças de grupo](../receitas/mudancas-de-grupo.md), [rejeições de conclusão](../receitas/rejeicoes-de-conclusao.md)

#### R-eventos-historico-05: O último evento registrado de uma encerrada é o de maior `idReqHist`, que é o evento de `ReqUltHistConcluida`. {#r-eventos-historico-05}
`ReqUltHistConcluida.idReqHist` aponta o maior `idReqHist` da requisição; o `idReqHist` é único por evento e crescente. O maior `idReqHist` é o último registrado e pode não ser o de maior data (registros offline chegam com data anterior); para o último por data, ordene por `dtFimReqHist` e desempate por `dtRegistro` (R-eventos-historico-03).
Receita: [quem encerrou](../receitas/quem-encerrou.md)

#### R-eventos-historico-06: Leia "última ação" de uma requisição em `ReqUltHist` (abertas) e `ReqUltHistConcluida` (encerradas). {#r-eventos-historico-06}
Cada tabela tem uma linha por requisição, com `idReqHist`, `dtUltHist`, `idUsu`, `idFrmAcao` e o rótulo `dsAcao` gravado. Algumas requisições abertas ainda não têm linha em `ReqUltHist` (sem nenhum evento); use `LEFT JOIN` a partir de `Req` quando a lista deve conter todas.
Receita: [quem encerrou](../receitas/quem-encerrou.md)

## 7. Views recomendadas

- `vwRepUltimaAcao`: última ação de cada requisição, abertas e encerradas, com `Quem` (nome do autor, ou "Execução Automática" quando `idUsu` é vazio ou não existe em `Usuario`), `Ação`, `dtAcao` e `Motivo`. Granularidade: uma linha por requisição que tenha linha em `ReqUltHist` ou `ReqUltHistConcluida`. Os dados vêm de `ReqUltHist`/`ReqUltHistConcluida` por `UNION ALL`, sem filtro. A ação vem do rótulo gravado (`dsAcao`), então para o código da ação ligue `idFrmAcao` a `FormAcao` e `Acao`.
- Para o histórico completo, as tabelas `ReqHistorico` e `ReqHistConcluida` com os `LEFT JOIN` da seção 5 são a recomendação.

## 8. Receitas

- [Mudanças de grupo](../receitas/mudancas-de-grupo.md)
- [Rejeições de conclusão](../receitas/rejeicoes-de-conclusao.md)
- [Quem encerrou](../receitas/quem-encerrou.md)

## Veja também

- [Fato: requisição](requisicao.md)
- [Fato: participação](participacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
