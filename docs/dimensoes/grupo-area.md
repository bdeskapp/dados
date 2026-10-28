---
gerado: sincronizacao
---
# Dimensão: grupo e área


Esta página descreve dois cadastros que a requisição aponta: o **grupo de atendimento** (`Grupo`) e a **área de atendimento** (`Area`). Descreve também o **grupo de acesso** (`GrupoAcesso`), que é outro cadastro, usado para permissão. A pessoa e a organização estão em [Pessoa e organização](pessoa-organizacao.md).

## 1. O que é na tela

| Na tela | Cadastro | Para que serve |
|---|---|---|
| Grupo (solucionador, "Solicitado" quando o participante é um grupo) | `Grupo` | equipe que atende requisições; recebe a requisição no direcionamento |
| Grupo de acesso | `GrupoAcesso` | conjunto de pessoas (e de outras entidades) que enxerga um formulário, um item de cardápio ou uma categoria |
| Área | `Area` | área de atendimento do catálogo de serviços; é a raiz da classificação `Area → Categoria → SubCategoria → Tarefa` |

`Grupo` e `GrupoAcesso` têm cada um a sua coluna `idGru` e a sua numeração: um mesmo número existe nos dois cadastros e identifica coisas diferentes. A chave estrangeira diz a qual dos dois a coluna pertence (seção 2).

## 2. Estrutura

### Grupo (atendimento)

| Coluna | Significado |
|---|---|
| `idGru` | identificador do grupo |
| `dsGru` | nome do grupo |
| `idAre` | área do grupo (`Area`); todo grupo tem uma área |
| `idUsu` | coordenador do grupo |
| `idCan` | calendário de atendimento do grupo (`CalendarioNome`) |
| `flgGruAtivo` | grupo ativo |
| `flgAtendeReq` | o grupo pode receber requisições |
| `flgDisponivel` | o grupo está disponível para receber |

- **Membros.** `UsuarioGrupo` liga usuário e grupo: uma linha por usuário e grupo, sem colunas de vigência. As colunas `flgAssume`, `flgAtribui` e `flgAdministra` dizem o que o membro pode fazer no grupo.
- **Hierarquia.** `Grupo` não tem coluna de grupo pai: os grupos formam uma lista plana, ligada a uma área.
- **Quem está sob a requisição.** Na participação, o grupo aparece quando o tipo do participante é `2` (Grupo): `ReqParticipante.idPart` aponta para `Grupo.idGru`. O papel (por exemplo o solicitado) vem de `idFrmPapel`. Veja [Papéis e participação](../mapa/papeis-e-participacao.md).

### Grupo de acesso (permissão)

| Coluna | Significado |
|---|---|
| `idGru` | identificador do grupo de acesso (numeração própria) |
| `dsGru` | nome |
| `idTpPapel` | tipo de entidade que o grupo admite como membro (`TipoPapel`) |
| `flgAtivo` | grupo de acesso ativo |
| `flgRestrito` | marca o grupo como restrito |

- **Membros.** `GrupoAcessoTipoPapel` guarda os membros: uma linha por grupo de acesso, entidade (`idPart`) e início (`dtInicio`). A vigência está em `dtFim`: membro vigente é `dtFim IS NULL`. A coluna `idUsu` é preenchida quando o membro é um usuário (tipo `1`) ou um gestor (tipo `8`), e então é igual a `idPart`; quando o membro é um contato (tipo `7`), recebe o `idUsu` do contato em `CRM_Contato`, preenchido quando o contato tem usuário; nos outros tipos as rotinas de associação deixam `idUsu` vazio. A pessoa chega ao grupo de acesso por `idUsu`: os membros dos tipos sem `idUsu` (grupo, hierarquia, entre outros) não viram pessoa, porque `vwReqAcessoInterna` (tipo `12`) e as consultas de acesso do produto filtram por `GrupoAcessoTipoPapel.idUsu`.
- **`GrupoAcessoUsuario`.** Guarda só usuários (`idGru`, `idUsu`, `dtInicio`, `dtFim`). O banco copia as inclusões, alterações e exclusões dela para `GrupoAcessoTipoPapel`. Quando uma única instrução grava várias linhas, só uma delas chega a `GrupoAcessoTipoPapel`. O produto, ao descobrir os grupos de acesso de um usuário, lê `GrupoAcessoTipoPapel`, que cobre todos os tipos de membro; por isso as consultas desta documentação usam essa tabela.
- **Onde o grupo de acesso é usado.** `FormAcesso` (formulário), `GrupoAcesso_ItemCardapio`, `GrupoAcesso_Categoria_ItemCardapio` e `GrupoAcessoFluxo` apontam para `GrupoAcesso.idGru`. Na participação, o tipo `12` (Grupo de Acesso) aponta `ReqParticipante.idPart` para `GrupoAcesso.idGru`.

### Área

| Coluna | Significado |
|---|---|
| `idAre` | identificador da área |
| `dsAre` | nome da área |
| `flgAreaAtiva` | área ativa |
| `idGruAdm`, `idGruKB` | grupos (`Grupo`) que administram a área e a base de conhecimento dela |

- **Quem aponta para `Area`** (chaves estrangeiras): `Formulario.idAre`, `Categoria.idAre` (obrigatória), `Grupo.idAre` (obrigatória), `Processo.idAre`, `KBase.idAre` e `Req.idAre`, entre outros.
- **Pessoa e área.** `Usuario` não tem coluna de área. A pessoa chega à área de dois modos: por `UsuarioGrupo → Grupo.idAre` (onde atende) e por `FormAcesso → GrupoAcesso → GrupoAcessoTipoPapel.idUsu` (o que enxerga e abre; só os membros com `idUsu` preenchido).
- **`Area.nmBanco`** é o nome do banco da área: o produto identifica a área ativa comparando essa coluna com o nome do banco em uso. Não entra nas consultas de negócio.

## 3. Como a requisição aponta para eles

| Coluna | Tabelas | Valor atual ou retrato | Pode vir vazia |
|---|---|---|---|
| `idGru` | `Req`, `ReqConcluida` | grupo gravado na abertura; em `Req` tem chave estrangeira; em `ReqConcluida` não há chave estrangeira | sim |
| `idGruAtual` | `Req`, `ReqConcluida` | **grupo atual**: acompanha o direcionamento; sem chave estrangeira nas duas tabelas | sim |
| `dsGru` | só `ReqConcluida` | **retrato**: nome do grupo `idGru` no momento do encerramento | sim |
| `idAre` | `Req`, `ReqConcluida` | área do **formulário** da requisição (é o `Formulario.idAre` gravado na abertura) | sim |
| `dsAre` | só `ReqConcluida` | **retrato**: nome da área `idAre` no encerramento | sim |

- **`idGru`.** Recebe o grupo informado na abertura. Na abertura `idGruAtual` recebe o mesmo valor.
- **`idGruAtual`.** No direcionamento e na devolução o produto grava o grupo do novo solicitado (papel `ADO`) quando ele é do tipo Grupo, e `NULL` quando é de outro tipo, como um usuário; na categorização e na transição que define grupo solucionador ele grava o grupo solucionador (detalhe em [Fato: requisição](../fatos/requisicao.md), seção 6). Por isso `idGruAtual` pode ser `NULL`, e pode diferir de `idGru` depois de um direcionamento. Na instalação de referência, todo `idGruAtual` preenchido de uma requisição aberta coincide com o grupo do participante vigente de papel `ADO` e tipo `2`.
- **Nome do grupo.** Para o grupo atual de uma aberta, junte `Grupo.dsGru`. Em `ReqConcluida`, `dsGru` guarda o nome do grupo `idGru` como estava no encerramento; o nome atual do mesmo grupo pode ser outro, porque o cadastro aceita renomear.
- **`idAre`.** Vem do formulário (em todas as linhas de `Req` com formulário, `Req.idAre = Formulario.idAre`). A área do grupo atual é `Grupo.idAre` de `idGruAtual`, e a área da classificação é `Categoria.idAre`, pela cadeia `Req.idTar → Tarefa.idCat → Categoria.idAre`. As três respondem perguntas diferentes e podem divergir. "Área da requisição" é a área do serviço pedido, `Req.idAre` (decisão do produto); o encerramento grava `dsAre` a partir dela. "Área de quem atende" é `Grupo.idAre`, e "área da categoria" é `Categoria.idAre`.
- **Retrato.** As colunas `dsGru` e `dsAre` entram no conjunto de retrato do encerramento descrito em [Abertas e encerradas](../mapa/abertas-e-encerradas.md).

## 4. Ativo e inativo

| Cadastro | Como identificar o ativo |
|---|---|
| `Grupo` | `flgGruAtivo = 1`; para listar o grupo que recebe requisições no direcionamento, acrescente `flgAtendeReq = 1`; o direcionamento tem três ramos: o dos grupos da atividade (`TarefaGrupo`) filtra `flgGruAtivo = 1` e `flgDisponivel = 1`, e os outros dois exigem também `flgAtendeReq = 1` |
| `GrupoAcesso` | `flgAtivo = 1` |
| Membro de `GrupoAcessoTipoPapel` | `dtFim IS NULL` |
| Membro de `UsuarioGrupo` | a linha existe; a tabela não tem vigência. O usuário ativo é o de `Usuario.flgUsuAtivo = 1` |
| `Area` | `flgAreaAtiva = 1` |

"Grupo ativo" numa métrica é só `flgGruAtivo = 1` (decisão do produto); `flgAtendeReq` e `flgDisponivel` são filtros de direcionamento.

## 5. Valores do produto

Os tipos de participante `2` (Grupo) e `12` (Grupo de Acesso) estão em [Valores definidos pelo produto](../dominios-do-produto.md), seção `TipoPapel`. Os nomes de grupos, grupos de acesso e áreas são cadastro do cliente.

## 6. Regras de uso

#### R-grupo-area-01: Leia `Grupo` para o atendimento e `GrupoAcesso` para a permissão, cada um pela chave estrangeira da coluna. {#r-grupo-area-01}
`Req.idGru`, `Req.idGruAtual`, `UsuarioGrupo.idGru` e `ReqHistorico.idGru` pertencem a `Grupo`; `FormAcesso.idGru` e `GrupoAcessoTipoPapel.idGru` pertencem a `GrupoAcesso`. A numeração dos dois cadastros é independente. `Req.idGruAtual` não tem chave estrangeira: aponta para `Grupo` porque o produto grava nela o `idPart` do solicitado do tipo Grupo, e na instalação de referência não há valor sem `Grupo` correspondente.
Receita: [requisições do grupo atual](../receitas/requisicoes-do-grupo-atual.md)

#### R-grupo-area-02: Para o grupo que tem a requisição agora, leia `idGruAtual` e o nome em `Grupo.dsGru`. {#r-grupo-area-02}
`idGruAtual` acompanha o direcionamento e pode ser `NULL` quando o solicitado é um usuário. `idGru` guarda o grupo da abertura.
Receita: [requisições do grupo atual](../receitas/requisicoes-do-grupo-atual.md)

#### R-grupo-area-03: Leia `ReqConcluida.dsGru` e `dsAre` como o nome do momento do encerramento. {#r-grupo-area-03}
O retrato guarda o nome que o cadastro tinha ao encerrar; para o nome de hoje, junte `Grupo` ou `Area` pelo id.

#### R-grupo-area-04: Use `LEFT JOIN` de `Req.idGru`, `idGruAtual` e `idAre` para o cadastro. {#r-grupo-area-04}
As três colunas aceitam valor vazio; o `LEFT JOIN` mantém as requisições sem grupo ou sem área.

#### R-grupo-area-05: Leia os membros de um grupo de acesso em `GrupoAcessoTipoPapel` com `dtFim IS NULL`. {#r-grupo-area-05}
A tabela guarda todos os tipos de membro; `idUsu` é preenchido quando o membro é um usuário (tipo `1`), um gestor (tipo `8`, igual a `idPart`) ou um contato com usuário (tipo `7`, com o `idUsu` do contato em `CRM_Contato`), e fica vazio nos outros tipos.

#### R-grupo-area-06: Junte `Usuario` com `flgUsuAtivo = 1` ao listar os membros de um grupo de atendimento. {#r-grupo-area-06}
`UsuarioGrupo` não tem vigência; o `JOIN` com `Usuario` traz o nome e o filtro de ativo.

#### R-grupo-area-07: Leia a área da requisição em `Req.idAre` (serviço pedido) e a área de quem atende em `Grupo.idAre` do grupo atual. {#r-grupo-area-07}
"Área da requisição" é a área do serviço pedido, `Req.idAre` (decisão do produto); o encerramento grava `dsAre` a partir dela. "Área de quem atende" é `Grupo.idAre` do grupo atual, e "área da categoria" é `Categoria.idAre` (veja [Classificação](classificacao.md)).

## 7. Views recomendadas

Para estes cadastros as consultas usam as tabelas; a documentação não recomenda view para grupo ou área. As views de participante e de acesso estão nas páginas de participação, e [views recomendadas](../views/views-recomendadas.md) reúne todas.

## 8. Receitas

- [Requisições do grupo atual](../receitas/requisicoes-do-grupo-atual.md)
- [Participantes vigentes](../receitas/participantes-vigentes.md)

## Veja também

- [Pessoa e organização](pessoa-organizacao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Fato: participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
