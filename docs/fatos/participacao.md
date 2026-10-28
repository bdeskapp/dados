---
gerado: sincronizacao
---
# Fato: participação


## 1. O que mede

Quem participou de cada requisição e em que papel: solicitante, atendente (solicitado), responsável, copiados, aprovadores e outros. Serve para responder "de quem é a requisição", "o que um usuário solicitou" e "quem atende".

## 2. Granularidade

Uma linha por requisição × participação. Uma participação é uma entidade (tipo `idTpPapel` e `idPart`) num papel (`idFrmPapel`), de `dtInicio` até `dtFim`. Uma requisição tem várias participações, e um mesmo papel pode ter mais de uma entidade vigente ao mesmo tempo (por exemplo, copiados `COP` em formulários com `FormPapel.flgMultiplo = 1`; o solicitado `ADO` tem `flgMultiplo = 0`). A chave é `idReqPart`. `FormPapel.flgMultiplo = 0` não garante um único participante vigente do papel: o esquema não tem restrição de unicidade sobre os participantes vigentes: em `ReqParticipante`, o único índice único é a chave primária, em `idReqPart`, e `flgMultiplo` é só uma coluna de `FormPapel`. Para escolher um, use o critério de `vwReq.nmUsuResponsavel`, que é do papel `RESP`: entre os vigentes (`dtFim IS NULL`), o primeiro por `dtInicio`. Esse critério não tem desempate; acrescente `idReqPart` quando a ordem precisa ser única.

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `ReqParticipante` | |
| Encerrada | `ReqPartConcluida` | acrescenta `dsPapel` (rótulo do papel) e `nmPart` (nome), gravados no encerramento |
| Nome exibido | `PartTipoPapel` | uma linha por (`idTpPapel`, `idPart`), com `nmPart` |
| Papel | `FormPapel` → `Papel` | `Papel.cdPapel` é o código do papel |
| Tipo | `TipoPapel` | |
| Quem pode ver | `vwReqAcessoTotal` | abertas e encerradas (ver [Papéis e participação](../mapa/papeis-e-participacao.md)) |

- **Quem grava.** Ao mudar de atendente, o produto insere a nova participação e preenche `dtFim` da que sai. No encerramento, as participações são copiadas para `ReqPartConcluida` só quando há linha em `PartTipoPapel` para (`idTpPapel`, `idPart`) e `FormPapel.flgAtivo = 1`: a participação que não atende às duas condições não é copiada. É um limite documentado (decisão do produto): quem não tem cadastro em `PartTipoPapel`, ou não tem papel ativo no formulário (`FormPapel.flgAtivo = 1`), falta em `ReqPartConcluida`. A parte encerrada das receitas de participação herda esse recorte.
- **Escolha de tabela.** Para listar participantes use `ReqParticipante` e `ReqPartConcluida` com `LEFT JOIN PartTipoPapel`; o par (`idTpPapel`, `idPart`) é a chave de `PartTipoPapel`, e o `LEFT JOIN` mantém cada participação uma única vez, com nome vazio quando a entidade não tem linha em `PartTipoPapel`.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReqPart` | identificador da participação | |
| `idReq` | requisição | |
| `idFrmPapel` | papel no formulário (`FormPapel`); leva a `Papel.cdPapel` | |
| `idTpPapel` | tipo do participante (`TipoPapel`) | |
| `idPart` | entidade participante; o destino depende do tipo | |
| `dtInicio` | início da participação | data e hora |
| `dtFim` | fim da participação; vazio enquanto vigente | data e hora |
| `FormPapel.dsPapel` | rótulo do papel no formulário | texto |
| `Papel.cdPapel` | código do papel ([Valores definidos pelo produto](../dominios-do-produto.md)) | |
| `PartTipoPapel.nmPart` | nome exibido da entidade | texto |

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Usuário | `idTpPapel` = 1: `idPart` → `Usuario.idUsu` |
| Grupo | `idTpPapel` = 2: `idPart` → `Grupo.idGru` |
| Gestor | `idTpPapel` = 8: `idPart` → `Usuario.idUsu` |
| Hierarquia | `idTpPapel` = 3: `idPart` → `OrgHierarquia.idHie` |
| Grupo de acesso | `idTpPapel` = 12: `idPart` → `GrupoAcesso.idGru` |
| Externo | `idTpPapel` = 13: `idPart` → `UsuarioExterno.idExt` |
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Tempo por grupo | o grupo do atendente vem de `ReqParticipante.idPart` quando `idTpPapel` = 2 (ver [Fato: tempo por grupo](tempo-por-grupo.md)) |

## 6. Regras de uso

#### R-participacao-01: Leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`. {#r-participacao-01}
`idTpPapel` diz o tipo do participante (usuário, grupo, sistema e assim por diante) e indica o destino de `idPart`; o papel está no caminho por `FormPapel`.
Receita: [solicitante e responsável](../receitas/solicitante-e-responsavel.md)

#### R-participacao-02: Filtre o participante vigente com `dtFim IS NULL`. {#r-participacao-02}
As tabelas guardam o histórico de participações. `vwParticipante` e `vwPartConcluida` expõem `dtFim` sem filtrar, e o filtro é escrito por quem consulta. Na encerrada, `ReqPartConcluida` não tem as participações de quem não tem cadastro em `PartTipoPapel` ou papel ativo no formulário (`FormPapel.flgAtivo = 1`), que a cópia do encerramento deixou de fora (seção 3, "Quem grava").
Receita: [participantes vigentes](../receitas/participantes-vigentes.md)

#### R-participacao-03: Leia `idPart` conforme o tipo. {#r-participacao-03}
Tipo `1` → `Usuario.idUsu`; tipo `2` → `Grupo.idGru`; tipo `8` (Gestor) → `Usuario.idUsu`; tipo `13` (Externo) → `UsuarioExterno.idExt`. Os tipos `3` e `12` estão na tabela da seção 5. Ligue a entidade com `LEFT JOIN` a partir da participação: as chaves estrangeiras de `ReqParticipante` são para `Req`, `FormPapel` e `TipoPapel`, e `idPart` não aponta por chave para a tabela do tipo; a participação cujo `idPart` não tem linha na tabela do tipo continua na lista, com os campos da entidade vazios.
Receita: [participantes vigentes](../receitas/participantes-vigentes.md)

#### R-participacao-04: Leia o nome exibido em `PartTipoPapel.nmPart`, por `LEFT JOIN` no par (`idTpPapel`, `idPart`). {#r-participacao-04}
Há participações cujo par ainda não tem linha em `PartTipoPapel`; o `LEFT JOIN` as mantém na lista. Na encerrada, `ReqPartConcluida.nmPart` é o nome gravado no encerramento, e as participações de quem não tem linha em `PartTipoPapel` ou papel ativo no formulário (`FormPapel.flgAtivo = 1`) não foram copiadas para ela (seção 3, "Quem grava").
Receita: [participantes vigentes](../receitas/participantes-vigentes.md)

#### R-participacao-05: Leia o rótulo do papel em `FormPapel.dsPapel` quando a pergunta é "como o formulário chama este papel". {#r-participacao-05}
`Papel.dsPapel` é o rótulo do papel no produto; `FormPapel.dsPapel` é o rótulo naquele formulário e pode diferir. `ReqPartConcluida.dsPapel` guarda o do formulário, para as participações que a cópia do encerramento levou (seção 3, "Quem grava").

#### R-participacao-06: Conte participações por `idReqPart` e requisições por `COUNT(DISTINCT idReq)`. {#r-participacao-06}
Um papel pode ter mais de uma entidade vigente na mesma requisição (por exemplo, copiados). Na encerrada, a contagem não inclui as participações que a cópia do encerramento deixou de fora (seção 3, "Quem grava").
Receita: [solicitante e responsável](../receitas/solicitante-e-responsavel.md)

## 7. Views recomendadas

- `vwReqAcessoTotal`: "quem pode ver" (ver [Papéis e participação](../mapa/papeis-e-participacao.md), seção 5). Use sempre filtrada por `idUsu` ou `idReq`.
- `vwReqAcesso` e `vwReqAcessoConcluida`: as duas metades de `vwReqAcessoTotal`, com a mesma granularidade, para quando a pergunta é só sobre abertas ou só sobre encerradas.

## 8. Receitas

- [Participantes vigentes](../receitas/participantes-vigentes.md)
- [Solicitante e responsável](../receitas/solicitante-e-responsavel.md)
- [Requisições de um solicitante](../receitas/requisicoes-de-um-solicitante.md)

## Veja também

- [Papéis e participação](../mapa/papeis-e-participacao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Fato: requisição](requisicao.md)
