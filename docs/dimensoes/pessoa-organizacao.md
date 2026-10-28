---
gerado: sincronizacao
---
# Dimensão: pessoa e organização


Esta página descreve quem é a pessoa (`Usuario`) e como a estrutura da organização é cadastrada: empresa, cargo, hierarquia organizacional e localização. Grupos e áreas estão em [Grupo e área](grupo-area.md).

## 1. O que é na tela

| Na tela | Cadastro |
|---|---|
| Usuário, nome, perfil, idioma | `Usuario` (`Perfil`, `Dominio`) |
| Empresa do usuário, cargo, departamento ou diretoria | `UsuarioHierarquia` (`Empresa`, `Cargo`, `OrgHierarquia`) |
| Nível da estrutura (por exemplo diretoria, gerência) | `OrgNivel`, com nomes que o cliente define |
| Localização | `Localiza` (`LocNivel`) |
| Solicitante externo (sem login) | `UsuarioExterno` |

## 2. Estrutura

### Usuário

| Coluna | Significado |
|---|---|
| `idUsu` | identificador do usuário |
| `nmUsu` | nome de exibição |
| `login` | login (seção "Login", abaixo); a tabela `Usuario` tem a coluna, e a view `vwUsuario` (`SELECT *` de `Usuario` com o acréscimo de `flgAtivo`) expõe as colunas que a tabela tinha quando a view foi criada, sem algumas das mais novas, como `idUsuOperacao` e `flgPermiteLoginBDesk` |
| `flgUsuAtivo` | usuário ativo |
| `dtIniUsu`, `dtFimUsu` | início e fim do cadastro |
| `idPer` | perfil (`Perfil`) |
| `idDom` | domínio de autenticação (`Dominio`); vazio indica senha nativa |
| `idLoc` | localização do usuário (`Localiza`) |
| `idUsuSuperiorHierarquico`, `idUsuSuperiorAlternativo` | superior do usuário (apontam para `Usuario`) |
| `flgAtendeReq`, `flgPartGrupo`, `flgAprovaReq` | marcas do cadastro (recebe requisições, participa de grupos, aprova) |
| `flgPermiteLoginBDesk` | permissão de login |

- **Login.** Quando `idDom` é vazio, o produto assume que o valor gravado em `login` tem um `x` na frente: remove o primeiro caractere ao exibir e acrescenta o `x` ao procurar. A convenção tem exceções: ao inativar o usuário pelo cadastro, o produto grava `*` na frente do `login`, e o valor passa a começar por `*`. Com domínio, o `login` é o próprio login. `login` não tem índice único; para identificar a pessoa use `idUsu`.
- **Consultas de negócio.** Para contar e agrupar pessoas bastam `idUsu`, `nmUsu` e `flgUsuAtivo`. As colunas de contato e de credencial (e-mail, telefones, documento pessoal, senha e tokens de acesso) são dado pessoal ou segredo, e ficam fora das consultas e dos relatórios.
- **Usuário externo.** `UsuarioExterno` (`idExt`, `nmExt`, `flgAtivo`) é outro cadastro. Na participação, é o tipo `13` (Externo): `ReqParticipante.idPart` aponta para `UsuarioExterno.idExt`. A ligação é a que o produto usa ao juntar as duas tabelas, e nenhuma participação do tipo `13` fica sem `UsuarioExterno` correspondente, nas abertas e nas encerradas, na instalação de referência.
- **Pessoa na requisição.** `Req` guarda só `idUsuOperacao`, o usuário logado na gravação. Solicitante, solicitado e demais pessoas ficam na [participação](../fatos/participacao.md), pelo tipo `1` (Usuário, `idPart` → `Usuario.idUsu`).

### Vínculo organizacional do usuário

`UsuarioHierarquia` tem uma linha por usuário (a chave é `idUsu`):

| Coluna | Aponta para |
|---|---|
| `idEmp` | `Empresa` (obrigatória) |
| `idCar` | `Cargo` |
| `idhie` | nó de `OrgHierarquia` |

- **Cargo.** `Cargo` (`idCar`, `dsCar`, `flgCarAtivo`) só se liga por `UsuarioHierarquia.idCar`; `Usuario` não tem coluna de cargo.
- **Usuário sem linha.** Um usuário pode não ter linha em `UsuarioHierarquia`; use `LEFT JOIN`.
- **`idDir`, `idDep`, `idCoo`.** São colunas de `UsuarioHierarquia` sem chave estrangeira e sem uso no código ou nos objetos programáveis; diretoria, departamento e coordenação são **níveis** da hierarquia (abaixo).

### Hierarquia organizacional (`OrgHierarquia`, `OrgNivel`)

- **`OrgHierarquia`** é uma árvore recursiva: `idHieAsc` aponta para o nó pai e é vazio na raiz. Pode haver várias raízes. Cada nó pertence a uma empresa (`idEmp`, obrigatória) e tem `dsHie` (nome), `sigla`, `ccustoHie` (centro de custo, texto livre), `idUsuResponsavel`, `dtIniHie`, `dtFimHie` e `dsHieComp` (caminho completo em texto).
- **`OrgNivel`** é o cadastro de níveis (`idNiv`, `cdNiv`, `dsNiv`). Cada nó aponta para o seu nível por `idNiv`. Os níveis são linhas de cadastro, e o **cliente** define a quantidade e os nomes.
- **Centro de custo.** É a coluna `ccustoHie` do nó; não há tabela de centro de custo.

### Empresa

`Empresa` (`idEmp`, `RazaoSocial`, `nmFantasia`, `flgEmpAtivo`, `flgCliente`, `flgFornecedor`) é o cadastro de empresas da instalação. `flgCliente` e `flgFornecedor` marcam o tipo da empresa. A empresa é um dado de cadastro e de relatório; o banco de cada cliente é separado pelo ambiente (host), e nenhuma tabela deste domínio tem coluna de cliente.

### Localização (`Localiza`, `LocNivel`)

`Localiza` é uma árvore recursiva como a hierarquia: `idLocAsc` aponta para o pai, `idLocNiv` para o nível (`LocNivel`), com `dsLoc`, `dsLocComp` (caminho completo), `dtIniLoc` e `dtFimLoc`.

## 3. Como a requisição aponta para eles

| Coluna | Tabelas | Valor atual ou retrato | Pode vir vazia |
|---|---|---|---|
| `idEmp` | `Req`, `ReqConcluida` | empresa do **beneficiado**, ou do solicitante quando não há beneficiado; gravada na abertura e atualizada nas abertas quando muda a empresa ou a hierarquia do usuário; no caminho de troca de participante pelo cadastro do usuário, o produto grava a empresa do usuário de `idUsu = 1` | sim |
| `idHie` | `Req`, `ReqConcluida` | nó de hierarquia do beneficiado ou do solicitante, gravado junto com `idEmp`; no caminho de troca de participante pelo cadastro do usuário, o produto grava o nó do usuário de `idUsu = 1` | sim; vem vazia quando o usuário não tem `idhie` |
| `idLoc` | `Req`, `ReqConcluida` | **valor atual editável**: na abertura automática, quando o formulário pede localização de sistema e a localização não vem fixa por mapeamento de cópia obrigatória (`tpCopiaLocalizacao = 1`; com `2` a cópia é opcional e a localização continua editável), o produto copia `Usuario.idLoc` (ou `Patrimonio.idLoc`) do participante do papel configurado em `FormLocaliza`. Na tela de abertura, esse valor é só uma sugestão, e o gravado é o que a tela envia. Depois, a alteração de localização da requisição pode mudá-lo. `Req.dsLoc` guarda o texto livre usado quando `idLoc` é vazio | sim; vem vazia quando o formulário não usa localização de sistema ou o participante não tem localização |
| `RazaoSocial` | só `ReqConcluida` | **retrato**: razão social de `idEmp` no encerramento | sim |
| `dsHie` | só `ReqConcluida` | **retrato**: `OrgHierarquia.dsHie` do nó `idHie` no encerramento (o nome do nó, sem o caminho `dsHieComp`) | sim |
| `dsLocSistema` | só `ReqConcluida` | **retrato**: `Localiza.dsLoc` de `idLoc` no encerramento | sim |

- **Quem grava `idEmp` e `idHie`.** O produto copia empresa e hierarquia do usuário que tem o papel `BEN` ou `ANTE`. A cópia acontece na abertura, na definição e na troca de participantes da requisição, e quando o cadastro de usuário muda a empresa ou a hierarquia da pessoa, caso em que atualiza as requisições abertas. Fora desses caminhos, a requisição não acompanha a mudança: importações e outras rotinas que mudam a organização da pessoa não atualizam a requisição. Na troca de participante pelo cadastro do usuário, o produto grava a empresa e a hierarquia do usuário de `idUsu = 1`.
- **Consequência.** `Req.idHie` e `idEmp` descrevem a organização da pessoa **na data em que o produto gravou**; as encerradas mantêm o último valor gravado. As colunas podem divergir do beneficiado ou solicitante vigente, porque dependem de a alteração passar por esses caminhos. Para a organização atual de uma pessoa, junte `UsuarioHierarquia` pela participação.
- **Retrato do encerramento.** O encerramento copia o nome de cada cadastro para a linha encerrada (`RazaoSocial`, `dsHie`, `dsLocSistema`). O cadastro pode ser renomeado depois; o retrato fica como era.
- As colunas de retrato fazem parte do conjunto de [Abertas e encerradas](../mapa/abertas-e-encerradas.md).

## 4. Ativo e inativo

| Cadastro | Como identificar o ativo |
|---|---|
| `Usuario` | `flgUsuAtivo = 1` (filtro do login e da lista de membros do produto) |
| `Empresa` | `flgEmpAtivo = 1` |
| `Cargo` | `flgCarAtivo = 1` |
| `Dominio` | `flgDomAtivo = 1` |
| `UsuarioExterno` | `flgAtivo = 1` |
| `OrgHierarquia` | `dtFimHie IS NULL` (a rotina que percorre a árvore filtra assim) |
| `Localiza` | `dtFimLoc IS NULL` |
| `OrgNivel`, `LocNivel` | `dtFimNiv IS NULL`, `dtFimLoc IS NULL` |

`OrgHierarquia` e `Localiza` não têm flag: o fim do nó é uma data.

## 5. Valores do produto

O tipo de participante `1` (Usuário), `3` (Hierarquia), `6` (Empresa) e `13` (Externo) estão em [Valores definidos pelo produto](../dominios-do-produto.md), seção `TipoPapel`. Perfis, cargos, empresas, níveis, hierarquias e localizações são cadastro do cliente.

## 6. Regras de uso

#### R-pessoa-organizacao-01: Identifique a pessoa por `idUsu` e filtre o usuário ativo por `flgUsuAtivo = 1`. {#r-pessoa-organizacao-01}
`login` não tem índice único e, sem domínio, o produto assume um `x` na frente do valor gravado (a convenção tem exceções, como o `*` gravado na frente do login ao inativar o usuário).

#### R-pessoa-organizacao-02: Leia empresa, cargo e nó da hierarquia da pessoa em `UsuarioHierarquia`, com `LEFT JOIN`. {#r-pessoa-organizacao-02}
`Usuario` não tem coluna de cargo, empresa ou hierarquia; um usuário pode não ter linha em `UsuarioHierarquia`, e `idCar` e `idhie` aceitam valor vazio.

#### R-pessoa-organizacao-03: Trate `OrgHierarquia` e `Localiza` como árvores recursivas por `idHieAsc` e `idLocAsc`. {#r-pessoa-organizacao-03}
O nível do nó vem de `OrgNivel` e `LocNivel`; os nomes dos níveis são do cliente.

#### R-pessoa-organizacao-04: Leia `Req.idEmp` e `Req.idHie` como a organização do beneficiado ou do solicitante gravada pelo produto na abertura, na troca de participantes e nas alterações do cadastro de usuário, que pode divergir da organização vigente. {#r-pessoa-organizacao-04}
As colunas aceitam valor vazio; `idHie` só vem preenchida quando o usuário tinha nó de hierarquia. Para a troca de participante pelo cadastro do usuário, a empresa e a hierarquia gravadas nesse caminho são as do usuário de `idUsu = 1`. Importações e outras rotinas que mudam a organização da pessoa não atualizam essas colunas. Para a organização do beneficiado ou solicitante, junte `UsuarioHierarquia` pela participação.

#### R-pessoa-organizacao-05: Leia `ReqConcluida.RazaoSocial`, `dsHie` e `dsLocSistema` como o nome do momento do encerramento. {#r-pessoa-organizacao-05}
Para o nome de hoje, junte `Empresa`, `OrgHierarquia` ou `Localiza` pelo id.

#### R-pessoa-organizacao-06: Chegue à pessoa de uma requisição pela participação (`idTpPapel = 1`, `idPart` → `Usuario.idUsu`). {#r-pessoa-organizacao-06}
`Req` não tem coluna de solicitante ou de atendente. Quando a pergunta pede uma linha por requisição, parta de `Req` (ou `ReqConcluida`) e traga a participação e `Usuario` com `LEFT JOIN`, para que a requisição sem participante do papel pedido continue no resultado. Quando pede uma linha por participação, como a receita abaixo, ligue a participação com `JOIN` e traga o nome com `LEFT JOIN`: a requisição sem participante do papel não tem linha a mostrar.
Receita: [solicitante e responsável](../receitas/solicitante-e-responsavel.md)

#### R-pessoa-organizacao-07: Selecione de `Usuario` só as colunas que a pergunta pede. {#r-pessoa-organizacao-07}
`idUsu`, `nmUsu` e `flgUsuAtivo` cobrem os relatórios de volume; contato e credencial são dado pessoal.

## 7. Views recomendadas

Para pessoa e organização as consultas usam as tabelas; a documentação não recomenda view para estes cadastros. [Views recomendadas](../views/views-recomendadas.md) reúne todas as views recomendadas.

## 8. Receitas

- [Requisições de um solicitante](../receitas/requisicoes-de-um-solicitante.md)
- [Solicitante e responsável](../receitas/solicitante-e-responsavel.md)
- [Participantes vigentes](../receitas/participantes-vigentes.md)

## Veja também

- [Grupo e área](grupo-area.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Fato: participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
