---
gerado: sincronizacao
---
# Fato: apontamento de horas e despesas


## 1. O que mede

O esforço e o gasto lançados numa requisição:

- o **apontamento**: horas que um usuário registra como trabalhadas na requisição (ação "Apontar Horas", código `APONT`), com a decisão de aprovação gravada à parte;
- a **despesa**: um valor em dinheiro reportado na requisição (ação "Reportar Despesa", código `REDESP`), com categoria, item e, se houver, fornecedor.

Os códigos das ações vêm de [domínios do produto](../dominios-do-produto.md).

## 2. Granularidade

- `ReqApontamento`: uma linha por apontamento (`idReqApont`, identidade). Uma requisição tem vários apontamentos, inclusive do mesmo usuário e do mesmo dia. `idSeq` não identifica o apontamento: é o número do grupo de apontamentos da requisição (seção 4).
- `ReqApontAprov`: no máximo uma linha por apontamento. A chave primária é `idReqApont`, que também é chave estrangeira para `ReqApontamento`. O apontamento sem linha aqui não tem decisão gravada; a tela o mostra como pendente.
- `ReqDespesa`: uma linha por despesa lançada (`idReqDesp`, identidade). Não há tabela de aprovação de despesa.

## 3. Tabelas

| Aberta | Encerrada | Conteúdo |
|---|---|---|
| `ReqApontamento` | `ReqApontConcluida` | o apontamento: requisição, participante, usuário, período, quantidade, data de gravação |
| `ReqApontAprov` | `ReqApontAprovConcluida` | a decisão sobre o apontamento: tipo, período e quantidade decididos, data e usuário da decisão; a encerrada traz também `nmUsuAprov` |
| `ReqDespesa` | `ReqDespConcluida` | a despesa: requisição, participante, usuário, datas, categoria, item, fornecedor, valor, documento, descrição; a encerrada traz também `nmUsu`, `dsCatDesp`, `dsItemDesp` e `RazaoSocial` |
| `CategoriaDespesa`, `ItemDespesa` | (mesma tabela) | cadastro de categorias (`dsCatDesp`) e de itens (`dsItemDesp`, com `idCatDesp`) |

**União recomendada:** [`vwReqApontTotal`, `vwReqApontAprovTotal` e `vwReqDespTotal`](../views/views-recomendadas.md) (aberta mais encerrada).

**Quem grava o apontamento.**
- A inclusão, a alteração e a exclusão pela tela inserem, atualizam e apagam a linha de `ReqApontamento`.
- A decisão de aprovação é gravada em `ReqApontAprov`. Quando a decisão é sobre um apontamento que ainda não existe (`idReqApont` zero) e traz quantidade maior que zero, ela insere também em `ReqApontamento`, desde que a linha traga `dtFim`: a linha nova sem `dtFim` (modo horas) é descartada em silêncio, sem gravar o apontamento nem a decisão. Quando insere, grava com `idUsuReporte` igual ao usuário que decidiu e o `idSeq` do apontamento anterior, e grava `ReqApontamentoHistorico` (`idReqApont`, `idReqHist`) quando há evento de histórico.
- A decisão tem o tipo `tpAprovacao`, domínio em [domínios do produto](../dominios-do-produto.md) (`ReqApontAprov.tpAprovacao`). Aprovado copia período e quantidade do apontamento; reprovado grava quantidade zero e datas vazias; parcial grava o período e a quantidade informados na decisão. Uma decisão com o valor `?` apaga a linha de `ReqApontAprov`, e o valor não é gravado.

**Modo de apontamento.** O formulário define se o apontamento é por período ou por horas (`Req.tpReporteHora`, copiado na abertura da requisição; domínio `Req.tpReporteHora` em [domínios do produto](../dominios-do-produto.md): período e horas). A inclusão e a alteração do apontamento gravam `dtFim` somente no modo período; a linha que nasce na decisão grava `dtFim` sempre. Por isso `dtFim` não indica o modo: leia `tpReporteHora` da requisição.

**Quem grava a despesa.** A inclusão da despesa insere em `ReqDespesa`; a alteração e a exclusão atualizam e apagam a linha. A cada inclusão, alteração ou exclusão, o produto soma ou subtrai o valor em `Req.CustoTotal`, lendo o valor atual da requisição e gravando o novo. `CustoTotal` é um acumulado incremental e não é recalculado a partir de `ReqDespesa`.

**Abertas e encerradas.** Os fatos ligam-se à requisição por `idReq` (`Req` ou `ReqConcluida`). O encerramento trata cada um de um jeito:
- **Apontamento e decisão em requisição fora de fluxo (`Req.idFlu` vazio).** O encerramento copia `ReqApontamento` e `ReqApontAprov` para o par encerrado e apaga as linhas de origem.
- **Apontamento e decisão em requisição de fluxo (`Req.idFlu` preenchido).** O encerramento da requisição não toca nas linhas, que ficam nas tabelas abertas. Quando é encerrada a requisição raiz do fluxo (`idFlu = idReq`), os apontamentos das requisições com aquele `idFlu` já presentes em `ReqConcluida` são copiados para o par encerrado e apagados das tabelas abertas. Até lá, `ReqApontamento` pode conter apontamentos de requisição que já está em `ReqConcluida`, e a tela os lê.
- **Despesa.** O encerramento copia só a despesa que tem usuário, categoria e item cadastrados, e grava na encerrada o nome do usuário, os rótulos de categoria e item e a razão social do fornecedor. Depois apaga todas as despesas da requisição de `ReqDespesa`, de modo que a despesa sem esses cadastros deixa de existir nas duas tabelas. As chaves estrangeiras de `ReqDespesa` para categoria e item (confiáveis) e para usuário (ativa, não confiável) impedem gravar despesa sem categoria, item ou usuário cadastrado; esse descarte só alcançaria uma linha gravada antes da chave estrangeira para usuário.

Detalhe e critérios: [Abertas e encerradas](../mapa/abertas-e-encerradas.md).

## 4. Colunas-chave

| Coluna | Significado | Unidade |
|---|---|---|
| `ReqApontamento.idReqApont` | identificador do apontamento | |
| `ReqApontamento.idReq` | requisição | |
| `ReqApontamento.idReqPart` | participante da requisição; o nome vem de `vwParticipante` no apontamento aberto e de `vwPartConcluida` no encerrado | |
| `ReqApontamento.idUsu` | usuário dono das horas; é a base do relatório de apontamento | |
| `ReqApontamento.idUsuReporte` | usuário que lançou o apontamento; quando a decisão cria a linha, é o usuário que decidiu | |
| `ReqApontamento.dtInicio`, `dtFim` | início e fim; `dtFim` é gravado no modo período e pela decisão (seção 3) | data e hora |
| `ReqApontamento.dtBase` | data de `dtInicio`, sem hora | data |
| `ReqApontamento.qtdHoras` | quantidade apontada; a duração do apontamento | minutos |
| `ReqApontamento.idSeq` | grupo de apontamentos da requisição: o apontamento novo recebe `Max(idSeq) + 1` e a linha criada pela decisão reaproveita o `idSeq` do apontamento anterior; o faturamento (`CRM_ApontCalc`, chave `idReq` e `idSeq`) e a tela agrupam por `idReq` e `idSeq`. A chave do apontamento é `idReqApont` | |
| `ReqApontAprov.tpAprovacao` | tipo da decisão; domínio em [domínios do produto](../dominios-do-produto.md) | código |
| `ReqApontAprov.qtdHoras` | quantidade decidida | minutos |
| `ReqApontAprov.idUsuAprov`, `dtAprovacao` | quem decidiu e quando | |
| `ReqDespesa.idReqDesp` | identificador da despesa | |
| `ReqDespesa.idReq`, `idReqPart`, `idUsu` | requisição, participante e usuário do lançamento | |
| `ReqDespesa.dtDespesa` | data em que a despesa ocorreu | data e hora |
| `ReqDespesa.dtRegistro` | momento do lançamento | data e hora |
| `ReqDespesa.idCatDesp`, `idItemDesp` | categoria e item | |
| `ReqDespesa.idFornecedor` | fornecedor, opcional (`Empresa.idEmp`) | |
| `ReqDespesa.valDespesa` | valor da despesa (tipo `MONEY`) | valor |
| `ReqDespesa.flgFatura` | marcação "Faturado sim/não" da despesa; ela não filtra o gasto, que soma todas as despesas (decisão do produto) | |

**Unidade de `qtdHoras`.** É minuto, apesar do nome. O produto descreve a quantidade apontada como "quantidade de horas apontadas em minutos" e, quando o apontamento chega com `dtInicio` e `dtFim` e quantidade zero, calcula `qtdHoras` como a diferença em minutos entre `dtInicio` e `dtFim`, tanto na inclusão quanto na decisão. A coluna é `SMALLINT`.

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq`; `ReqDespesa.idReq` tem chave estrangeira para `Req`. `ReqApontamento` pode pertencer a requisição já presente em `ReqConcluida` (seção 3) |
| Tempo e calendário | `ReqApontamento.dtBase` ou `dtInicio`; `ReqDespesa.dtDespesa` (data da despesa) ou `dtRegistro` (data do lançamento) |
| Grupo | pelo grupo atual da requisição: `Req.idGruAtual` ou `ReqConcluida.idGruAtual` → `Grupo.idGru` |
| Usuário | `ReqApontamento.idUsu` (dono das horas), `ReqApontamento.idUsuReporte` (quem lançou), `ReqApontAprov.idUsuAprov`, `ReqDespesa.idUsu` → `Usuario.idUsu`; só `ReqApontAprov.idUsuAprov` e `ReqDespesa.idUsu` têm FK para `Usuario` |
| Participação | `idReqPart` → `ReqParticipante.idReqPart` (requisição aberta; a despesa tem chave estrangeira para ela) ou `ReqPartConcluida.idReqPart` (requisição encerrada) |
| Despesa | `ReqDespesa.idCatDesp` → `CategoriaDespesa.idCatDesp`; `idItemDesp` → `ItemDespesa.idItemDesp`; `idFornecedor` → `Empresa.idEmp` |
| Modo de apontamento | `Req.tpReporteHora` ou `ReqConcluida.tpReporteHora` |

Classificação, status, prioridade e canal vêm da requisição: veja a [matriz fato × dimensão](../mapa/matriz-fato-dimensao.md).

## 6. Regras de uso

#### R-apontamento-e-despesas-01: Leia `qtdHoras` como minutos e divida por 60 para apresentar horas. {#r-apontamento-e-despesas-01}
O produto grava `qtdHoras` em minutos, em `ReqApontamento` e em `ReqApontAprov`. O relatório de apontamento soma `qtdHoras` direto, em minutos, e `vwRepApontamento` divide por 60 para chegar a horas. O nome da coluna não indica a unidade.

#### R-apontamento-e-despesas-02: Tome a duração do apontamento em `qtdHoras`. {#r-apontamento-e-despesas-02}
`dtFim` é gravado no modo período e pela decisão, e a inclusão do apontamento não o grava no modo horas; `dtFim` não carrega a duração em todos os modos. `qtdHoras` tem a duração em todos eles. O modo está em `Req.tpReporteHora` (ou `ReqConcluida.tpReporteHora`).

#### R-apontamento-e-despesas-03: Ligue a decisão ao apontamento por `ReqApontAprov.idReqApont` com `LEFT JOIN`, leia a rejeição por `tpAprovacao` e compare lançado com decidido só no agregado. {#r-apontamento-e-despesas-03}
`ReqApontAprov` tem no máximo uma linha por apontamento; a ausência de linha é apontamento sem decisão. A quantidade decidida 0 não significa reprovado: o tipo da decisão diz (a reprovação grava zero, e, no modo horas, a tela de decisão redistribui a quantidade parcial informada entre as linhas do grupo antes de gravá-las). Compare `ReqApontamento.qtdHoras` com `ReqApontAprov.qtdHoras` somados por requisição, usuário e dia, e não linha a linha.

#### R-apontamento-e-despesas-04: Identifique o apontamento por `idReqApont` e use `idSeq` como grupo de apontamentos da requisição. {#r-apontamento-e-despesas-04}
A decisão reaproveita o `idSeq` do apontamento anterior, então várias linhas de uma requisição repartem o mesmo `idSeq`. Juntar duas tabelas por (`idReq`, `idSeq`) multiplica linhas; junte por `idReqApont`.

#### R-apontamento-e-despesas-05: Cubra a requisição em qualquer estado pelas views de união, e leia o apontamento de requisição de fluxo na tabela aberta até o encerramento do fluxo. {#r-apontamento-e-despesas-05}
`vwReqApontTotal`, `vwReqApontAprovTotal` e `vwReqDespTotal` unem aberta e encerrada sem filtro. Numa requisição de fluxo, apontamentos e decisões ficam nas tabelas abertas, mesmo com a requisição em `ReqConcluida`, até o encerramento da requisição raiz do fluxo. A despesa sem cadastro de usuário, categoria ou item não existe na encerrada ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).

#### R-apontamento-e-despesas-06: Some `valDespesa` por `idCatDesp` e `idItemDesp`; o gasto da requisição é a soma de `valDespesa`. {#r-apontamento-e-despesas-06}
`ReqDespConcluida` traz `dsCatDesp` e `dsItemDesp` copiados no encerramento; nas abertas, o rótulo vem de `CategoriaDespesa` e `ItemDespesa`. O fornecedor é opcional (`idFornecedor` vazio): ligue `Empresa` por `LEFT JOIN`. O gasto soma todas as despesas, sem afirmar moeda, e `flgFatura` é só a marcação "Faturado sim/não" (decisão do produto). `Req.CustoTotal` é um acumulado incremental.

## 7. Views recomendadas

- `vwReqApontTotal`, `vwReqApontAprovTotal` e `vwReqDespTotal`: aberta mais encerrada, uma linha por apontamento, decisão e despesa. Detalhe em [Views recomendadas](../views/views-recomendadas.md).

## 8. Receitas

Sem receita nesta versão.

## Veja também

- [Fato: requisição](requisicao.md)
- [Fato: participação](participacao.md)
- [Pessoa e organização](../dimensoes/pessoa-organizacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
