---
gerado: sincronizacao
---
# Regras essenciais das dimensões


Uma linha por regra `R-…` das páginas de dimensões, agrupadas por página, com o título da regra e o link para a âncora. A explicação de cada regra e a receita que a aplica estão na página dona. Total: 41 regras. As regras dos fatos estão em [regras essenciais](regras-essenciais.md) (62 regras).

## Dimensão: calendário de atendimento

Página: [Dimensão: calendário de atendimento](../dimensoes/tempo-calendario.md)

- [R-tempo-calendario-01](../dimensoes/tempo-calendario.md#r-tempo-calendario-01): Chegue ao calendário de atraso, de avanço e do intervalo final por `idGruAtual` → `Grupo.idCan`; `Req.sla` segue o grupo do momento do cálculo.
- [R-tempo-calendario-02](../dimensoes/tempo-calendario.md#r-tempo-calendario-02): Entenda um dia não útil como uma linha de `Calendario` com `dtCal` preenchida e sem horário.
- [R-tempo-calendario-03](../dimensoes/tempo-calendario.md#r-tempo-calendario-03): Leia `Feriado` como o cadastro de feriados que alimenta `Calendario`.
- [R-tempo-calendario-04](../dimensoes/tempo-calendario.md#r-tempo-calendario-04): Entenda que a alteração de calendário ou de grupo recalcula as requisições abertas afetadas.

## Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)

Página: [Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)](../dimensoes/classificacao.md)

- [R-classificacao-01](../dimensoes/classificacao.md#r-classificacao-01): Leia a classificação de uma aberta por `Req.idTar → Tarefa`: a categoria da atividade é `Tarefa.idCat` e a subcategoria é `Tarefa.idSca`.
- [R-classificacao-02](../dimensoes/classificacao.md#r-classificacao-02): Ligue `Req.idTar` a `Tarefa` com `LEFT JOIN`.
- [R-classificacao-03](../dimensoes/classificacao.md#r-classificacao-03): Leia a classificação de uma encerrada nas colunas de retrato de `ReqConcluida`.
- [R-classificacao-04](../dimensoes/classificacao.md#r-classificacao-04): Leia a área da requisição em `Req.idAre` e a área da categoria em `Categoria.idAre`.
- [R-classificacao-05](../dimensoes/classificacao.md#r-classificacao-05): Leia as categorias de um formulário em `FormCategoria` (muitos-para-muitos), entre outros filtros das listas.
- [R-classificacao-06](../dimensoes/classificacao.md#r-classificacao-06): O cadastro de classificação inclui itens inativos que requisições antigas ainda referenciam.

## Dimensão: status

Página: [Dimensão: status](../dimensoes/status-fase.md)

- [R-status-fase-01](../dimensoes/status-fase.md#r-status-fase-01): Leia o status pelo código `Status.cdSta` (`Req.idFrmStatus → FormStatus.idSta → Status.cdSta`).
- [R-status-fase-02](../dimensoes/status-fase.md#r-status-fase-02): Ligue `Req.idFrmStatus` a `FormStatus` com `LEFT JOIN`.
- [R-status-fase-03](../dimensoes/status-fase.md#r-status-fase-03): Leia o status de uma encerrada em `ReqConcluida.idFrmStatus` e o rótulo gravado em `ReqConcluida.dsSta`.
- [R-status-fase-04](../dimensoes/status-fase.md#r-status-fase-04): Leia a requisição cancelada pelo código `CL`.
- [R-status-fase-05](../dimensoes/status-fase.md#r-status-fase-05): Leia o estado pela tabela: aberta é estar em `Req`, mesmo em status terminal; a passagem para `ReqConcluida` acontece no status terminal.

## Dimensão: grupo e área

Página: [Dimensão: grupo e área](../dimensoes/grupo-area.md)

- [R-grupo-area-01](../dimensoes/grupo-area.md#r-grupo-area-01): Leia `Grupo` para o atendimento e `GrupoAcesso` para a permissão, cada um pela chave estrangeira da coluna.
- [R-grupo-area-02](../dimensoes/grupo-area.md#r-grupo-area-02): Para o grupo que tem a requisição agora, leia `idGruAtual` e o nome em `Grupo.dsGru`.
- [R-grupo-area-03](../dimensoes/grupo-area.md#r-grupo-area-03): Leia `ReqConcluida.dsGru` e `dsAre` como o nome do momento do encerramento.
- [R-grupo-area-04](../dimensoes/grupo-area.md#r-grupo-area-04): Use `LEFT JOIN` de `Req.idGru`, `idGruAtual` e `idAre` para o cadastro.
- [R-grupo-area-05](../dimensoes/grupo-area.md#r-grupo-area-05): Leia os membros de um grupo de acesso em `GrupoAcessoTipoPapel` com `dtFim IS NULL`.
- [R-grupo-area-06](../dimensoes/grupo-area.md#r-grupo-area-06): Junte `Usuario` com `flgUsuAtivo = 1` ao listar os membros de um grupo de atendimento.
- [R-grupo-area-07](../dimensoes/grupo-area.md#r-grupo-area-07): Leia a área da requisição em `Req.idAre` (serviço pedido) e a área de quem atende em `Grupo.idAre` do grupo atual.

## Dimensão: pessoa e organização

Página: [Dimensão: pessoa e organização](../dimensoes/pessoa-organizacao.md)

- [R-pessoa-organizacao-01](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-01): Identifique a pessoa por `idUsu` e filtre o usuário ativo por `flgUsuAtivo = 1`.
- [R-pessoa-organizacao-02](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-02): Leia empresa, cargo e nó da hierarquia da pessoa em `UsuarioHierarquia`, com `LEFT JOIN`.
- [R-pessoa-organizacao-03](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-03): Trate `OrgHierarquia` e `Localiza` como árvores recursivas por `idHieAsc` e `idLocAsc`.
- [R-pessoa-organizacao-04](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-04): Leia `Req.idEmp` e `Req.idHie` como a organização do beneficiado ou do solicitante gravada pelo produto na abertura, na troca de participantes e nas alterações do cadastro de usuário, que pode divergir da organização vigente.
- [R-pessoa-organizacao-05](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-05): Leia `ReqConcluida.RazaoSocial`, `dsHie` e `dsLocSistema` como o nome do momento do encerramento.
- [R-pessoa-organizacao-06](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-06): Chegue à pessoa de uma requisição pela participação (`idTpPapel = 1`, `idPart` → `Usuario.idUsu`).
- [R-pessoa-organizacao-07](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-07): Selecione de `Usuario` só as colunas que a pergunta pede.

## Dimensão: prioridade e SLA

Página: [Dimensão: prioridade e SLA](../dimensoes/prioridade-sla.md)

- [R-prioridade-sla-01](../dimensoes/prioridade-sla.md#r-prioridade-sla-01): Leia o rótulo do nível de impacto e de urgência pela definição do formulário.
- [R-prioridade-sla-02](../dimensoes/prioridade-sla.md#r-prioridade-sla-02): Trate `nPrioridade`, `nImp` e `nUrg` como números sem chave estrangeira.
- [R-prioridade-sla-03](../dimensoes/prioridade-sla.md#r-prioridade-sla-03): Meça "estourou o prazo" pelas datas previstas.
- [R-prioridade-sla-04](../dimensoes/prioridade-sla.md#r-prioridade-sla-04): Leia `sla` como minutos de calendário do grupo.

## Dimensão: canal e origem

Página: [Dimensão: canal e origem](../dimensoes/canal-origem.md)

- [R-canal-origem-01](../dimensoes/canal-origem.md#r-canal-origem-01): Leia o canal de abertura em `tpAgenteReg` e some abertas e encerradas.
- [R-canal-origem-02](../dimensoes/canal-origem.md#r-canal-origem-02): Leia a origem do contato em `Req.idFrmOrigem → FormOrigem.dsFrmOrigem`, e o rótulo de uma encerrada em `ReqConcluida.dsFrmOrigem`.
- [R-canal-origem-03](../dimensoes/canal-origem.md#r-canal-origem-03): Trate o canal vazio como parte do resultado.

## Dimensão: ação

Página: [Dimensão: ação](../dimensoes/acao.md)

- [R-acao-01](../dimensoes/acao.md#r-acao-01): Leia o código da ação por `ReqHistorico.idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- [R-acao-02](../dimensoes/acao.md#r-acao-02): Leia o texto exibido da ação em `FormAcao.dsAcao` e o texto do catálogo em `Acao.dsAcao`.
- [R-acao-03](../dimensoes/acao.md#r-acao-03): Conte mudança de grupo como cada ação `DIR` do histórico e rejeição de conclusão como cada ação `REJCON`.
- [R-acao-04](../dimensoes/acao.md#r-acao-04): Leia "quem encerrou" como o autor da ação que levou a requisição ao status terminal.
- [R-acao-05](../dimensoes/acao.md#r-acao-05): Leia `ATR` como "Atribuir Responsabilidade" e `ATRR` como "Atribuir Responsável" no catálogo.

## Veja também

- [Regras essenciais dos fatos](regras-essenciais.md)
- [Matriz fato × dimensão](matriz-fato-dimensao.md)
- [INDEX](../busca.md)
