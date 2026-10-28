---
gerado: sincronizacao
---
# Dimensão: classificação (categoria, subcategoria, atividade, formulário e item de cardápio)


## 1. O que é na tela

Ao abrir ou recategorizar uma requisição, a tela pede, nesta ordem, **Categoria**, **Sub Categoria** e **Atividade** (rótulos da tela de recategorização). A **Atividade** é a tabela `Tarefa` do banco, e `Req.idTar` guarda a escolha. Acima da categoria existe a **Área** (`Area`). Separado da árvore, o **Formulário** (`Formulario`) é o tipo de requisição que se abre, e o **Item de cardápio** (`ItemCardapio`) é um atalho de abertura.

## 2. Estrutura

```
Area (idAre) 1 --< Categoria (idCat, idAre) 1 --< SubCategoria (idSca, idCat) 1 --< Tarefa (idTar, idSca)
                         ^
                         | muitos-para-muitos: FormCategoria (idFrm, idCat)
                  Formulario (idFrm)
```

| Nível | Tabela | Chave | Liga ao nível acima por | Ativo / disponível |
|---|---|---|---|---|
| Área | `Area` | `idAre` | | `flgAreaAtiva` |
| Categoria | `Categoria` | `idCat` | `Categoria.idAre` | `flgCatAtivo`, `flgDisponivel` |
| Subcategoria | `SubCategoria` | `idSca` | `SubCategoria.idCat` | `flgScaAtivo`, `flgDisponivel` |
| Atividade | `Tarefa` | `idTar` | `Tarefa.idSca` e `Tarefa.idCat` | `flgTarAtivo`, `flgDisponivel` |

- São quatro níveis fixos. Nenhuma das tabelas tem coluna de pai recursivo.
- `Tarefa` guarda `idSca` (subcategoria) e `idCat` (categoria). **A categoria da atividade é `Tarefa.idCat`** e a subcategoria é `Tarefa.idSca`: é o par que o produto lê e que o encerramento grava no retrato. O banco não obriga `Tarefa.idCat` a ser igual a `SubCategoria.idCat`; as duas colunas podem divergir. A tela de abertura navega pela árvore por `SubCategoria.idCat` e `Tarefa.idSca`, enquanto a lista de atividades por formulário, o retrato do encerramento e o SLA usam `Tarefa.idCat`; quando as duas colunas divergem, a categoria mostrada na tela difere da gravada.
- `Tarefa` não tem `idFrm`: a atividade não pertence a um formulário. O formulário oferece categorias, e as atividades vêm dessas categorias.

### Formulário e categoria: muitos-para-muitos

`FormCategoria` liga formulário a categoria (chave primária `idFrm` + `idCat`). Um formulário oferece várias categorias, e uma categoria é oferecida por vários formulários. A tela de abertura lista as categorias de `FormCategoria` do formulário escolhido que estejam ativas e disponíveis nos dois lados e que tenham subcategoria e atividade ativas e disponíveis. A lista de atividades aplica, entre outros filtros, `Tarefa.flgRecat = 0`, `Tarefa.flgSomenteFluxo = 0` (só quando a lista é pedida para um processo) e, quando `Formulario.flgFiltrarTipoTarefa = 1`, o tipo de atividade em `FormTipoTarefa`. O vínculo de hoje não impede que uma requisição guarde uma atividade de formulário sem categoria em `FormCategoria`.

### Formulário

- `Formulario` (`idFrm`) é o tipo de requisição: o que o solicitante abre. Tem `cdFrm` e `vsFrm` (código e versão), `dsFrm` (nome) e `idAre` (área do formulário).
- Está **ativo** com `flgFrmAtivo = 1` e **disponível** para abertura com `flgFrmDisponivel = 1`; as listas de abertura exigem os dois.
- Define também as listas por formulário de status, ações, papéis e origens (`FormStatus`, `FormAcao`, `FormPapel`, `FormOrigem`), descritas em [Status](status-fase.md), [Ação](acao.md) e [Canal e origem](canal-origem.md).

### Item de cardápio

- `ItemCardapio` (`Id`, bigint) é um atalho de abertura: nome amigável, formulário (`idFrm`) e o XML `MetaDados`.
- A abertura por item lê do `MetaDados` os metadados nomeados `Formulario` e `Atividade`. O item escolhe formulário e atividade; ele não é um quinto nível da árvore.
- Está ativo com `Ativo = 1`; as listas do cardápio filtram por esse campo.
- A tabela `Requisicao` (pedido do cardápio) é outro objeto; as requisições estão em `Req` e `ReqConcluida`.

## 3. Como a requisição aponta para a classificação

| Coluna | Em `Req` (aberta) | Em `ReqConcluida` (encerrada) | Valor atual ou retrato | Pode vir vazia |
|---|---|---|---|---|
| `idTar` | atividade | atividade (sem chave estrangeira), copiada de `vwTarefa` no encerramento | atual: o cadastro de hoje; na encerrada, o valor gravado no encerramento | sim |
| `idCat`, `idSca` | não existem | existem | retrato do encerramento | sim, quando `idTar` é vazio |
| `dsCat`, `dsSca`, `dsTar` | não existem | existem | retrato do encerramento | sim, quando `idTar` é vazio |
| `idAre` | área do formulário | área do formulário | gravada na abertura | sim |
| `dsAre` | não existe | existe | retrato do encerramento | sim |
| `idFrm` | formulário | formulário (sem chave estrangeira) | gravado na abertura | não |
| `idItemCardapio` | item | item | gravado na abertura | sim |

- **`Req` não tem `idCat` nem `idSca`.** A categoria e a subcategoria de uma aberta vêm de `Req.idTar → Tarefa.idCat` e `Tarefa.idSca`.
- **`idTar` pode estar vazia.** A abertura grava `NULL` quando nenhuma atividade foi escolhida. Por isso a ligação com `Tarefa` é um `LEFT JOIN`, e a receita marca essas requisições como sem atividade.
- **Aberta × encerrada.** O encerramento copia a classificação de `vwTarefa` para `ReqConcluida.idCat`, `dsCat`, `idSca`, `dsSca`, `dsTar` e o nome da área para `dsAre` ([Abertas e encerradas](../mapa/abertas-e-encerradas.md), seção 5). `vwTarefa` liga `Tarefa` a `SubCategoria`, `Categoria`, `Area` e `TipoTarefa` por `INNER JOIN`, e o encerramento a lê por `LEFT OUTER JOIN`: uma atividade com cadastro incompleto nessa cadeia encerra com `idTar` e retrato vazios. A encerrada guarda os rótulos da época; se uma categoria for renomeada depois, a aberta mostra o nome novo e a encerrada o nome gravado.
- **Área.** `Req.idAre` é a área do **formulário** (`Formulario.idAre`, gravada na abertura), e `ReqConcluida.dsAre` é o nome dessa mesma `idAre`. A área da árvore é `Categoria.idAre`, outra coluna.
- **Recategorização.** `ReqRecat` e `ReqRecatConcluida` guardam a mudança de atividade (`idTarAnt`, `idTarAtual`, `dtRecat`); a ação `RECAT` regrava `Req.idTar`. O detalhe do evento fica em [Fato: eventos do histórico](../fatos/eventos-historico.md).

## 4. Ativo e inativo

- `Area` tem só `flgAreaAtiva`; categoria, subcategoria e atividade têm `flg...Ativo` e `flgDisponivel`. As listas da tela de abertura exigem os dois iguais a 1.
- A exclusão de uma categoria grava os dois campos em 0; o registro continua no banco.
- Requisições antigas continuam apontando para atividade, categoria ou formulário que já não estão ativos. Para contar o histórico, leia os cadastros sem filtrar por ativo.

## 5. Valores do produto

Não há lista de valores do produto nesta dimensão: áreas, categorias, subcategorias, atividades, formulários e itens de cardápio são cadastros de cada instalação.

## 6. Regras de uso

#### R-classificacao-01: Leia a classificação de uma aberta por `Req.idTar → Tarefa`: a categoria da atividade é `Tarefa.idCat` e a subcategoria é `Tarefa.idSca`. {#r-classificacao-01}
`Req` guarda só a atividade. O retrato da encerrada e o produto usam o mesmo par de colunas de `Tarefa`. A área da categoria é `Categoria.idAre`.
Receita: [volume por classificação](../receitas/volume-por-classificacao.md)

#### R-classificacao-02: Ligue `Req.idTar` a `Tarefa` com `LEFT JOIN`. {#r-classificacao-02}
`idTar` aceita vazio, e o `LEFT JOIN` mantém as requisições sem atividade, que a receita marca numa coluna própria.
Receita: [volume por classificação](../receitas/volume-por-classificacao.md)

#### R-classificacao-03: Leia a classificação de uma encerrada nas colunas de retrato de `ReqConcluida`. {#r-classificacao-03}
`idCat`, `dsCat`, `idSca`, `dsSca` e `dsTar` guardam o que valia no encerramento; `idCat` e `idSca` também são retrato, e uma atividade pode ter mudado de subcategoria ou de categoria entre encerramentos. Rótulos ou ids diferentes para o mesmo `idTar` geram linhas diferentes. O total por atividade soma as linhas por `idTar`; o total por categoria soma por `idCat`.
Receita: [volume por classificação](../receitas/volume-por-classificacao.md)

#### R-classificacao-04: Leia a área da requisição em `Req.idAre` e a área da categoria em `Categoria.idAre`. {#r-classificacao-04}
"Área da requisição" é a área do serviço pedido, `Req.idAre`, que vem do formulário (decisão do produto); o encerramento grava `dsAre` a partir dela. "Área da categoria" é `Categoria.idAre`, e "área de quem atende" é `Grupo.idAre`. As colunas respondem a perguntas diferentes e podem apontar para áreas diferentes.

#### R-classificacao-05: Leia as categorias de um formulário em `FormCategoria` (muitos-para-muitos), entre outros filtros das listas. {#r-classificacao-05}
`Tarefa` não tem `idFrm`; a atividade chega ao formulário pela categoria. As listas da tela ainda aplicam `FormTipoTarefa`, `flgRecat`, `flgSomenteFluxo` (só quando a lista é de um processo) e o estado ativo e disponível. O vínculo de hoje não prova a categoria vigente na abertura: a requisição guarda só a atividade.

#### R-classificacao-06: O cadastro de classificação inclui itens inativos que requisições antigas ainda referenciam. {#r-classificacao-06}
As condições `flg...Ativo = 1` e `flgDisponivel = 1` descrevem o que a tela oferece hoje; requisições antigas apontam para cadastros inativos, e a leitura histórica usa o cadastro inteiro.

## 7. Views recomendadas

Nenhuma view entra para a pergunta "árvore de classificação", porque a documentação só recomenda view que responde a pergunta inteira: a página recomenda as quatro tabelas, que mantêm as requisições sem atividade e os cadastros inativos.

## 8. Receitas

- [Volume por classificação](../receitas/volume-por-classificacao.md)

## Veja também

- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Status](status-fase.md)
- [Canal e origem](canal-origem.md)
