---
gerado: sincronizacao
---
# INDEX

Porta de entrada da documentação. Comece por aqui: a pergunta de negócio, o termo de tela ou a tabela leva à página. **Confirme o significado de cada coluna na página do fato ou da dimensão antes de usar.**

A página [pendências](limitacoes-conhecidas.md) guarda as decisões de produto que as páginas citam.

## 1. Por pergunta de negócio

Cada pergunta leva à receita, à página do fato (ou da dimensão) e às views recomendadas de [Views recomendadas](views/views-recomendadas.md).

### Volume e classificação

- **Quantas requisições foram abertas em cada mês, somando abertas e encerradas?** Receita [volume-por-mes](receitas/volume-por-mes.md); fato [requisição](fatos/requisicao.md); mapa [abertas e encerradas](mapa/abertas-e-encerradas.md); views: [`vwReq` e `vwReqTotal`](views/views-recomendadas.md).
- **Quantas requisições foram abertas em cada categoria, subcategoria e atividade?** Receita [volume-por-classificacao](receitas/volume-por-classificacao.md); dimensão [classificação](dimensoes/classificacao.md); fato [requisição](fatos/requisicao.md); views: nenhuma (a receita parte das tabelas).
- **Quantas requisições foram abertas por cada canal?** Receita [volume-por-canal](receitas/volume-por-canal.md); dimensão [canal e origem](dimensoes/canal-origem.md); fato [requisição](fatos/requisicao.md); views: nenhuma (a receita parte das tabelas).
- **Quais requisições têm um determinado grupo como grupo atual?** Receita [requisicoes-do-grupo-atual](receitas/requisicoes-do-grupo-atual.md); fato [requisição](fatos/requisicao.md); dimensão [grupo e área](dimensoes/grupo-area.md); views: nenhuma (a receita parte das tabelas).

### Tempos e prazos

- **Quanto tempo cada grupo ficou com as requisições?** Receita [tempo-atendimento-por-grupo](receitas/tempo-atendimento-por-grupo.md); fato [tempo por grupo](fatos/tempo-por-grupo.md); views: nenhuma (a receita parte das tabelas).
- **Qual o tempo total gravado para cada requisição?** Receita [tempo-total-por-requisicao](receitas/tempo-total-por-requisicao.md); fato [tempo da requisição](fatos/tempo-requisicao.md); views: nenhuma (a receita parte das tabelas).
- **Quanto tempo as encerradas levaram da abertura ao encerramento, em cada categoria?** Receita [tempo-abertura-ate-encerramento-por-categoria](receitas/tempo-abertura-ate-encerramento-por-categoria.md); fato [tempo da requisição](fatos/tempo-requisicao.md); dimensão [classificação](dimensoes/classificacao.md); views: nenhuma (a receita parte das tabelas).
- **Quanto tempo as requisições levaram até a primeira resposta?** Receita [tempo-ate-primeira-resposta](receitas/tempo-ate-primeira-resposta.md); fatos [marcos](fatos/marcos.md) e [tempo da requisição](fatos/tempo-requisicao.md); views: nenhuma (a receita parte das tabelas).
- **Quanto tempo as requisições passaram em cada status?** Receita [tempo-em-cada-status](receitas/tempo-em-cada-status.md); fato [tempo por status](fatos/tempo-por-status.md); dimensão [status e fase](dimensoes/status-fase.md); views: [`vwRepTimeStatus`](views/views-recomendadas.md).
- **Que percentual das requisições de cada grupo foi encerrado dentro do prazo?** Receita [sla-por-grupo](receitas/sla-por-grupo.md); fato [marcos](fatos/marcos.md); dimensão [prioridade e SLA](dimensoes/prioridade-sla.md); views: nenhuma (a receita parte das tabelas).
- **Quantas requisições ficaram fora do prazo em cada prioridade?** Receita [fora-do-sla-por-prioridade](receitas/fora-do-sla-por-prioridade.md); fato [marcos](fatos/marcos.md); dimensão [prioridade e SLA](dimensoes/prioridade-sla.md); views: nenhuma (a receita parte das tabelas).
- **Que requisições abertas de um grupo já passaram do prazo neste momento?** Receita [atrasadas-agora](receitas/atrasadas-agora.md); fato [marcos](fatos/marcos.md); views: nenhuma (a receita parte das tabelas).

### Eventos do histórico

- **Quem executou a ação que levou cada requisição ao estado final?** Receita [quem-encerrou](receitas/quem-encerrou.md); fato [eventos do histórico](fatos/eventos-historico.md); dimensão [ação](dimensoes/acao.md); views: nenhuma (a receita parte das tabelas).
- **Quantas vezes uma requisição foi direcionada, e quantos direcionamentos tiveram as requisições de cada grupo?** Receita [mudancas-de-grupo](receitas/mudancas-de-grupo.md); fato [eventos do histórico](fatos/eventos-historico.md); views: nenhuma (a receita parte das tabelas).
- **Quais requisições tiveram a conclusão rejeitada, quando e por quem?** Receita [rejeicoes-de-conclusao](receitas/rejeicoes-de-conclusao.md); fato [eventos do histórico](fatos/eventos-historico.md); dimensão [ação](dimensoes/acao.md); views: nenhuma (a receita parte das tabelas).
- **Qual a taxa de rejeição de conclusão das requisições encerradas de cada grupo?** Receita [taxa-de-rejeicao-por-grupo](receitas/taxa-de-rejeicao-por-grupo.md); fato [eventos do histórico](fatos/eventos-historico.md); dimensão [ação](dimensoes/acao.md); views: nenhuma (a receita parte das tabelas).

### Participação

- **Quem participa agora de uma requisição, em que papel e com que nome?** Receita [participantes-vigentes](receitas/participantes-vigentes.md); fato [participação](fatos/participacao.md); mapa [papéis e participação](mapa/papeis-e-participacao.md); views: nenhuma (a receita parte das tabelas).
- **Quais requisições tiveram um determinado usuário como solicitante?** Receita [requisicoes-de-um-solicitante](receitas/requisicoes-de-um-solicitante.md); fato [participação](fatos/participacao.md); views: nenhuma (a receita parte das tabelas).
- **Quem é o solicitante e quem é o responsável das requisições de um grupo?** Receita [solicitante-e-responsavel](receitas/solicitante-e-responsavel.md); fato [participação](fatos/participacao.md); views: nenhuma (a receita parte das tabelas).
- **Quem foi o último atendente a agir em cada requisição aberta?** Receita [ultimo-atendente-das-abertas](receitas/ultimo-atendente-das-abertas.md); fatos [eventos do histórico](fatos/eventos-historico.md) e [participação](fatos/participacao.md); views: nenhuma (a receita parte das tabelas).
- **Como achar o `idUsu` de uma pessoa?** Filtre `Usuario.nmUsu` e confirme o `idUsu` antes de usá-lo nas receitas; dimensão [pessoa e organização](dimensoes/pessoa-organizacao.md).

### Dados adicionais

- **Que valor cada requisição tem num determinado dado adicional?** Receita [valores-de-um-campo](receitas/valores-de-um-campo.md); fato [dados adicionais](fatos/dados-adicionais.md); views: nenhuma (a receita parte das tabelas).
- **Como ver os valores de vários dados adicionais lado a lado?** Receita [pivo-de-campos](receitas/pivo-de-campos.md); fato [dados adicionais](fatos/dados-adicionais.md); views: nenhuma (a receita parte das tabelas).
- **Quantas requisições escolheram cada item de um campo de lista?** Receita [distribuicao-campo-lista](receitas/distribuicao-campo-lista.md); fato [dados adicionais](fatos/dados-adicionais.md); views: nenhuma (a receita parte das tabelas).
- **Em que formulários um dado adicional está configurado e tem valor?** Receita [formularios-que-usam-campo](receitas/formularios-que-usam-campo.md); fato [dados adicionais](fatos/dados-adicionais.md); views: nenhuma (a receita parte das tabelas).
- **Como achar o `idDad` de um dado adicional pelo nome?** Filtre `DadoAdicional.dsDad` e confirme o `idDad` antes de usá-lo nas receitas; fato [dados adicionais](fatos/dados-adicionais.md).

### Vínculos e avaliação

- **Quais requisições são filhas diretas de uma requisição pai?** Receita [filhas-de-um-pai](receitas/filhas-de-um-pai.md); fato [vínculos](fatos/vinculos.md); views: nenhuma (a receita parte das tabelas).
- **Como os grupos foram avaliados, e qual a parcela das encerradas, sem as canceladas (`CL`), que recebeu avaliação, e qual a taxa de nota entre os registros de `ReqAvaliacao`?** Receita [avaliacoes-por-grupo](receitas/avaliacoes-por-grupo.md); fato [avaliação e satisfação](fatos/avaliacao-satisfacao.md); views: nenhuma (a receita parte das tabelas).

### Apontamento e despesas

- **Quantas horas foram apontadas e quanto se gastou em despesas em cada requisição?** Fato [apontamento e despesas](fatos/apontamento-e-despesas.md); views: `vwReqApontTotal`, `vwReqApontAprovTotal` e `vwReqDespTotal` ([views recomendadas](views/views-recomendadas.md)).

## 2. Por termo de tela

Os termos de tela e a coluna que alimenta cada um ficam em [Glossário: termo na tela e coluna no banco](glossario-tela-banco.md), com as colunas termo na tela, onde aparece, `tabela.coluna` (com o tratamento que a tela dá ao valor, quando há) e página.

## 3. Por tabela ou view

Em ordem alfabética, cada objeto leva à página dona.

- `Acao`: [Dimensão: ação](dimensoes/acao.md)
- `Area`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `Calendario`: [Dimensão: calendário de atendimento](dimensoes/tempo-calendario.md)
- `CalendarioNome`: [Dimensão: calendário de atendimento](dimensoes/tempo-calendario.md)
- `CalendarioUpdate`: [Dimensão: calendário de atendimento](dimensoes/tempo-calendario.md)
- `Cargo`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `Categoria`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `CategoriaDespesa`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `DadConjunto`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadContextoCampo`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadDominio`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadEntidade`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadoAdicional`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadValor`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `DadValorDominio`: [Fato: dados adicionais](fatos/dados-adicionais.md)
- `Dominio`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `Empresa`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `Feriado`: [Dimensão: calendário de atendimento](dimensoes/tempo-calendario.md)
- `FormAcao`: [Dimensão: ação](dimensoes/acao.md)
- `FormAcaoMotivo`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `FormCategoria`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `FormOrigem`: [Dimensão: canal e origem](dimensoes/canal-origem.md)
- `FormOrigemAcesso`: [Dimensão: canal e origem](dimensoes/canal-origem.md)
- `FormPapel`: [Papéis e participação](mapa/papeis-e-participacao.md)
- `FormPri`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `FormPriMatriz`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `FormSLA`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `FormStatus`: [Dimensão: status](dimensoes/status-fase.md)
- `FormTransicao`: [Dimensão: status](dimensoes/status-fase.md)
- `Formulario`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `Grupo`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `GrupoAcesso`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `GrupoAcessoTipoPapel`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `GrupoAcessoUsuario`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `Impacto`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `ImpactoNivel`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `ItemCardapio`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `ItemDespesa`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `Localiza`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `LocNivel`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `OrgHierarquia`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `OrgNivel`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `Papel`: [Papéis e participação](mapa/papeis-e-participacao.md)
- `Parametro`: [Dimensão: calendário de atendimento](dimensoes/tempo-calendario.md)
- `PartTipoPapel`: [Papéis e participação](mapa/papeis-e-participacao.md)
- `Perfil`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `PesqOpcao`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `PesqPergunta`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `PesqRespCab`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `PesqResposta`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `Pesquisa`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `Req`: [Fato: requisição](fatos/requisicao.md); também [Abertas e encerradas](mapa/abertas-e-encerradas.md) e [Fato: marcos da requisição](fatos/marcos.md)
- `ReqApontamento`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqApontamentoHistorico`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqApontAprov`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqApontAprovConcluida`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqApontConcluida`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqAvaliacao`: [Fato: avaliação e satisfação](fatos/avaliacao-satisfacao.md)
- `ReqConcluida`: [Fato: requisição](fatos/requisicao.md); também [Abertas e encerradas](mapa/abertas-e-encerradas.md) e [Fato: marcos da requisição](fatos/marcos.md)
- `ReqDespConcluida`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqDespesa`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `ReqHistConcluida`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `ReqHistorico`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `ReqPartConcluida`: [Fato: participação](fatos/participacao.md)
- `ReqParticipante`: [Fato: participação](fatos/participacao.md)
- `ReqPlanoAlerta`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `ReqRecat`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `ReqRecatConcluida`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `ReqStatus`: [Fato: tempo por status](fatos/tempo-por-status.md)
- `ReqStatusConcluida`: [Fato: tempo por status](fatos/tempo-por-status.md)
- `ReqTime`: [Fato: tempo da requisição](fatos/tempo-requisicao.md)
- `ReqTimeAdo`: [Fato: tempo de atendimento por grupo](fatos/tempo-por-grupo.md)
- `ReqTimeAdoConcluida`: [Fato: tempo de atendimento por grupo](fatos/tempo-por-grupo.md)
- `ReqTimeConcluida`: [Fato: tempo da requisição](fatos/tempo-requisicao.md)
- `ReqUltHist`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `ReqUltHistConcluida`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `ReqVinculada`: [Fato: vínculos entre requisições](fatos/vinculos.md)
- `ReqVinculadaRef`: [Fato: vínculos entre requisições](fatos/vinculos.md)
- `Status`: [Dimensão: status](dimensoes/status-fase.md)
- `SubCategoria`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `Tarefa`: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](dimensoes/classificacao.md)
- `TipoPapel`: [Papéis e participação](mapa/papeis-e-participacao.md)
- `TipoSla`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `TipoVinculo`: [Fato: vínculos entre requisições](fatos/vinculos.md)
- `Urgencia`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `UrgenciaNivel`: [Dimensão: prioridade e SLA](dimensoes/prioridade-sla.md)
- `Usuario`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `UsuarioExterno`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `UsuarioGrupo`: [Dimensão: grupo e área](dimensoes/grupo-area.md)
- `UsuarioHierarquia`: [Dimensão: pessoa e organização](dimensoes/pessoa-organizacao.md)
- `Vinculo`: [Fato: vínculos entre requisições](fatos/vinculos.md)
- `vwRepTimeStatus`: [Fato: tempo por status](fatos/tempo-por-status.md)
- `vwRepUltimaAcao`: [Fato: eventos do histórico](fatos/eventos-historico.md)
- `vwReq`: [Fato: requisição](fatos/requisicao.md); também em [Abertas e encerradas](mapa/abertas-e-encerradas.md)
- `vwReqAcesso`: [Fato: participação](fatos/participacao.md)
- `vwReqAcessoConcluida`: [Fato: participação](fatos/participacao.md)
- `vwReqAcessoTotal`: [Fato: participação](fatos/participacao.md); também em [Papéis e participação](mapa/papeis-e-participacao.md)
- `vwReqApontAprovTotal`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `vwReqApontTotal`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `vwReqDespTotal`: [Fato: apontamento de horas e despesas](fatos/apontamento-e-despesas.md)
- `vwReqTotal`: [Fato: requisição](fatos/requisicao.md); também em [Abertas e encerradas](mapa/abertas-e-encerradas.md)


Mapas e modelo: [modelo](mapa/modelo.md), [matriz fato × dimensão](mapa/matriz-fato-dimensao.md), [regras essenciais](mapa/regras-essenciais.md) (fatos) e [das dimensões](mapa/regras-essenciais-dimensoes.md), [abertas e encerradas](mapa/abertas-e-encerradas.md), [papéis e participação](mapa/papeis-e-participacao.md), [views recomendadas](views/views-recomendadas.md) e [pendências abertas](limitacoes-conhecidas.md).

## 4. Fora de escopo

Assuntos que a documentação não detalha, com a página que explica o limite: [push](fora-de-escopo/push.md), [workflow](fora-de-escopo/workflow.md), [CMDB](fora-de-escopo/cmdb.md), [CRM](fora-de-escopo/crm.md), [chatbot](fora-de-escopo/chatbot.md), [e-mail](fora-de-escopo/email.md), [base de conhecimento](fora-de-escopo/base-de-conhecimento.md) e [motor de relatórios](fora-de-escopo/motor-de-relatorios.md).
