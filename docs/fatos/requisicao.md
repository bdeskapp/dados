---
gerado: sincronizacao
---
# Fato: requisição


## 1. O que mede

A requisição é o centro do modelo: cada chamado, solicitação ou tarefa registrada no BDesk. Contar linhas desta página dá o **volume** de requisições; as demais páginas de fatos (participação, tempos, histórico) se ligam a ela por `idReq`.

## 2. Granularidade

Uma linha por requisição. `idReq` identifica a requisição e não se repete entre as duas tabelas.

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `Req` | requisições em andamento |
| Encerrada | `ReqConcluida` | requisições encerradas, com colunas de retrato do encerramento |
| Ambas | `vwReq`, `vwReqTotal` | `UNION ALL` das duas tabelas, uma linha por requisição |

- **Quem grava.** A abertura insere a linha em `Req`. Quando a requisição chega a um status terminal, o encerramento copia a requisição para `ReqConcluida` e apaga a linha de `Req`. Detalhes em [Abertas e encerradas](../mapa/abertas-e-encerradas.md).
- **Quando.** No momento da abertura e no momento do encerramento.
- **`vwReq` e `vwReqTotal`.** Cobrem abertas e encerradas, uma linha por requisição, com `LEFT JOIN` em `FormStatus` (a requisição sem status continua na lista). A coluna `ReqStatus` informa a tabela de origem (`Aberta` ou `Encerrada`). `vwReqTotal` acrescenta a coluna `dsReq` (descrição completa). Em `dsSta`, a linha aberta mostra o rótulo atual do status e a encerrada mostra o rótulo gravado no encerramento. Escolha `vwReq` quando a descrição não é necessária.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReq` | identificador da requisição | |
| `idFrm` | formulário da requisição (`Formulario`) | |
| `dsTitulo` | título | texto |
| `dsReq` | descrição | texto |
| `dtAbertura` | data e hora de abertura (sempre preenchida) | data e hora |
| `dtFimReal` | data e hora de encerramento real | data e hora |
| `idFrmStatus` | status da requisição no formulário (`FormStatus`) | |
| `idTar` | atividade (`Tarefa`); pode ficar vazia | |
| `idGru` | grupo gravado na abertura | |
| `idGruAtual` | grupo atual (seção 6) | |
| `idFlu` | fluxo ao qual a requisição pertence (seção 7) | |
| `idFrmOrigem` | origem da abertura (`FormOrigem`) | |
| `idEmp` | empresa (`Empresa`) | |
| `idHie` | posição na hierarquia organizacional (`OrgHierarquia`) | |
| `idItemCardapio` | item do cardápio que originou a requisição (`ItemCardapio`) | |

As colunas de datas de prazo e de tempos têm página própria: [Marcos](marcos.md) e [Tempo da requisição](tempo-requisicao.md).

### Colunas de retrato do encerramento

`ReqConcluida` guarda, além das colunas comuns, os rótulos e a classificação gravados no momento do encerramento: `dsSta`, `dsAre`, `idCat`, `dsCat`, `idSca`, `dsSca`, `dsTar`, `SlaReal` (copiada no encerramento e regravada depois só quando alguém executa manualmente o cálculo das encerradas sem linha em `ReqTimeConcluida`; ver [Tempo da requisição](tempo-requisicao.md)), `dsGru`, `dsFrmOrigem`, `dsLocSistema`, `nmPat`, `numeroPat`, `seriePat`, `dsHie` e `RazaoSocial`. A tabela com a origem de cada uma está em [Abertas e encerradas](../mapa/abertas-e-encerradas.md). `dsGru` é o nome do grupo `idGru`. `Req` tem `tpAgend` e `idUsuOperacao`, que `ReqConcluida` não tem.

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Status | `Req.idFrmStatus` → `FormStatus.idSta` → `Status.cdSta`; use o código `cdSta`, porque o rótulo `FormStatus.dsSta` é definido por formulário |
| Classificação (atividade, subcategoria, categoria) | aberta: `Req.idTar` → `Tarefa` (use `LEFT JOIN`, porque `idTar` pode ficar vazia); encerrada: retrato em `ReqConcluida` |
| Grupo | `idGruAtual` → `Grupo.idGru` (grupo atual); `idGru` → `Grupo.idGru` (grupo da abertura) |
| Pessoas | por [participação](participacao.md): `ReqParticipante` e `ReqPartConcluida` |

## 6. Grupo atual

- Na abertura, `idGruAtual` recebe o mesmo valor de `idGru`.
- No direcionamento e na devolução, o produto grava em `idGruAtual` o grupo do novo solicitado (papel `ADO`) quando ele é de tipo Grupo, e `NULL` quando o novo solicitado é de outro tipo, como um usuário.
- Na recategorização (ação `RECAT`), quando o grupo muda, a requisição é direcionada de novo e `idGruAtual` é gravado como no direcionamento.
- Na categorização, o produto grava em `idGruAtual` o grupo solucionador definido na categorização.
- Por isso `idGruAtual` pode ser `NULL`: a requisição cujo solicitado atual não é um grupo (um usuário, por exemplo) não aparece como requisição do grupo atual de nenhum grupo.
- Na transição de status que define grupo solucionador, o registro de histórico aplica a troca de grupo solucionador para qualquer ação do evento, exceto no evento de abertura pela integração com o Zabbix, que não a aplica. Quando existe grupo solucionador para o status e a ação e ele difere do atual, primeiro, se o calendário muda (tipo de SLA tempo decorrido), `dtFimPrev` é recalculado, com ou sem `ADO` vigente. Depois os participantes `ADO`, `SHADO` e `RESP` vigentes são encerrados um a um; no `ADO`, o novo solicitado é inserido e `idGruAtual` recebe o grupo de `FormTransGrupoSolucionador`. Sem `ADO` vigente, `idGruAtual` não muda.
- Na encerrada, `idGruAtual` guarda o último valor.

## 7. Fluxo (`idFlu`)

`Req.idFlu` tem chave estrangeira para `Workflow.idFlu`; `idFluPai` aponta para o fluxo pai. As requisições com `idFlu = idReq` são as raízes dos fluxos. Para o motor de workflow, ver "motor de workflow (fora de escopo)".

## 8. Regras de uso

#### R-requisicao-01: Some abertas e encerradas para qualquer volume histórico. {#r-requisicao-01}
`Req` guarda as requisições em andamento e `ReqConcluida` as encerradas; as duas não têm `idReq` em comum. `vwReq` já traz as duas.
Receita: [volume por mês](../receitas/volume-por-mes.md)

#### R-requisicao-02: Leia o estado (aberta ou encerrada) pela tabela de origem, e o status pelo código `Status.cdSta`. {#r-requisicao-02}
A coluna `ReqStatus` de `vwReq` e `vwReqTotal` repete a tabela de origem (`Aberta` ou `Encerrada`); o status da requisição é outro dado. Uma requisição cancelada está em `Req` ou em `ReqConcluida`, com o status `CL`.
Receita: [volume por mês](../receitas/volume-por-mes.md)

#### R-requisicao-03: Leia a classificação de uma encerrada nas colunas de retrato de `ReqConcluida`, e a de uma aberta em `Tarefa`. {#r-requisicao-03}
`Req` guarda a atividade em `idTar`. `ReqConcluida` guarda `idCat`, `dsCat`, `idSca`, `dsSca` e `dsTar` como estavam no encerramento, copiados de `vwTarefa`. O `idTar` de `ReqConcluida` vem da mesma view, que liga `Tarefa` por `INNER JOIN` a `SubCategoria`, `Categoria`, `Area` e `TipoTarefa`: a atividade com cadastro incompleto nesses vínculos encerra com `idTar` e as colunas de retrato vazios.

#### R-requisicao-04: Use `LEFT JOIN` ao ligar `Req.idTar` a `Tarefa`. {#r-requisicao-04}
`idTar` aceita valor vazio, e o `LEFT JOIN` mantém as requisições sem atividade.

#### R-requisicao-05: Leia o grupo atual em `idGruAtual` e o nome em `Grupo.dsGru`. {#r-requisicao-05}
`ReqConcluida.dsGru` é o nome do grupo `idGru` (da abertura) gravado no encerramento.
Receita: [requisições do grupo atual](../receitas/requisicoes-do-grupo-atual.md)

#### R-requisicao-06: Leia o estado da requisição pela tabela em que ela está; a mudança de tabela acontece quando uma transição leva ao status terminal. {#r-requisicao-06}
A requisição passa para `ReqConcluida` quando uma transição de status a leva a um status sem transição de saída em `FormTransicao`, por qualquer ação: a mudança de tabela acompanha a transição, e a requisição que está em `Req` continua aberta mesmo que o status dela não tenha transição de saída. Uma requisição com status `CN` ou `CL` continua em `Req` quando o status tem transição de saída no formulário dela. `CONC` e `ENC` têm o mesmo efeito (encerram quando levam a status final) e só o rótulo muda (decisão do produto; ver [Ação](../dimensoes/acao.md)).

## 9. Views recomendadas

`vwReq` e `vwReqTotal` (seção 3). A página [views recomendadas](../views/views-recomendadas.md) reúne todas.

## 10. Receitas

- [Volume por mês](../receitas/volume-por-mes.md)
- [Requisições de um solicitante](../receitas/requisicoes-de-um-solicitante.md)
- [Requisições do grupo atual](../receitas/requisicoes-do-grupo-atual.md)

## Veja também

- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Fato: participação](participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
