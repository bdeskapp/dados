---
gerado: sincronizacao
---
# Dimensão: canal e origem


Há duas colunas diferentes na requisição, e cada uma responde a uma pergunta: o **canal** (`tpAgenteReg`) diz por qual mecanismo do sistema a requisição foi aberta, e a **origem** (`idFrmOrigem`) diz de onde veio o contato, conforme a lista cadastrada no formulário.

## 1. O que é na tela

- **Origem**: ao abrir uma requisição, o atendente escolhe, entre as origens cadastradas para o formulário, de onde veio o contato (`FormOrigem.dsFrmOrigem`).
- **Canal**: não tem campo na tela de abertura; o sistema grava o código conforme o caminho de abertura (telas de atendimento ou desdobramento, e-mail, abertura de fluxo, agenda recorrente, tela de pedido do portal web ou API).

## 2. Canal: `Req.tpAgenteReg`

- Coluna `CHAR(1)`, sem tabela de apoio e sem chave estrangeira, nas duas tabelas (`Req.tpAgenteReg` e `ReqConcluida.tpAgenteReg`); admite `NULL`.
- O código é gravado na abertura da requisição, com o valor recebido, e fica `NULL` quando vem vazio. A abertura pela tela de pedido do portal web ou pela API grava `X`. O desdobramento grava `M`, seja ele feito pelas telas de atendimento, seja pelo serviço de integração. As tarefas simples da web não informam o canal e gravam `NULL`. As telas de abertura do atendimento gravam `M`, e a tela de abertura de fluxo grava `P`. O encerramento copia o valor para `ReqConcluida`.
- O valor é o da abertura: nenhuma rotina do produto altera a coluna depois.

### Valores do produto

Códigos e rótulos de [Valores definidos pelo produto](../dominios-do-produto.md), seção "Req.tpAgenteReg". O código é um literal gravado pelo produto, e o rótulo descreve o caminho de abertura (decisão do produto):

| `tpAgenteReg` | Canal |
|---|---|
| `A` | automática |
| `E` | e-mail |
| `M` | abertura pelas telas de atendimento ou por desdobramento |
| `P` | processo (fluxo): rotina automática e tela de abertura de fluxo |
| `R` | agenda recorrente |
| `X` | abertura pela tela de pedido do portal web ou pela API |
| `NULL` | sem código gravado |

Requisições de fluxo (processo) recebem também outros códigos de canal, além de `P`. Para identificar requisição de fluxo, filtre `Req.idFlu` preenchido (e `ReqConcluida.idFlu`); `P` marca a abertura de requisição de fluxo pela rotina automática e pela tela de abertura de fluxo.

## 3. Origem: `Req.idFrmOrigem → FormOrigem`

| Item | Detalhe |
|---|---|
| Tabela | `FormOrigem` (`idFrmOrigem`, `dsFrmOrigem`, `idFrm`, `flgSistema`, `flgDisponivel`, `flgAtivo`) |
| Liga à requisição por | `Req.idFrmOrigem`; em `ReqConcluida`, `idFrmOrigem` sem chave estrangeira |
| Escopo | por formulário: cada linha de `FormOrigem` pertence a um `idFrm`; a origem de uma requisição é do formulário dela |
| Quem cadastra | a instalação: a tela de abertura só oferece origens com `flgSistema = 0`, `flgAtivo = 1` e `flgDisponivel = 1`, liberadas por grupo de acesso em `FormOrigemAcesso` |
| Pode vir vazia | sim, nas duas tabelas |
| Atual ou retrato | `Req`: o rótulo vem de `FormOrigem`; `ReqConcluida.dsFrmOrigem` é o retrato do rótulo no encerramento |

Os rótulos de origem são cadastro de cada instalação e não têm lista do produto.

## 4. Ativo e inativo

Origem ativa: `FormOrigem.flgAtivo = 1`; disponível: `flgDisponivel = 1`. Requisições antigas continuam apontando para origens inativas; para contar o histórico, ligue `FormOrigem` sem filtro.

## 5. Regras de uso

#### R-canal-origem-01: Leia o canal de abertura em `tpAgenteReg` e some abertas e encerradas. {#r-canal-origem-01}
A coluna existe nas duas tabelas, com os códigos de [Valores definidos pelo produto](../dominios-do-produto.md); o código `NULL` aparece como uma linha com `canal` vazio, e a tradução em rótulo é a tabela da seção 2.
Receita: [volume por canal](../receitas/volume-por-canal.md)

#### R-canal-origem-02: Leia a origem do contato em `Req.idFrmOrigem → FormOrigem.dsFrmOrigem`, e o rótulo de uma encerrada em `ReqConcluida.dsFrmOrigem`. {#r-canal-origem-02}
A origem é cadastro do formulário, escolhido pelo atendente; o canal é gravado pelo sistema. Cada coluna responde a uma pergunta.

#### R-canal-origem-03: Trate o canal vazio como parte do resultado. {#r-canal-origem-03}
A abertura grava `NULL` quando o código não é informado, e a receita mostra essas requisições numa linha própria.
Receita: [volume por canal](../receitas/volume-por-canal.md)

## 6. Views recomendadas

`vwReq` e `vwReqTotal` não trazem `tpAgenteReg`; a página recomenda as tabelas `Req` e `ReqConcluida`.

## 7. Receitas

- [Volume por canal](../receitas/volume-por-canal.md)

## Veja também

- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Classificação](classificacao.md)
