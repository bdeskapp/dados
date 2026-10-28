---
gerado: sincronizacao
---
# Papéis e participação


Quem participa de uma requisição fica em `ReqParticipante` (abertas) e `ReqPartConcluida` (encerradas). Cada linha responde a três perguntas diferentes, e cada uma tem a sua coluna.

## 1. Tipo, papel e entidade

| Pergunta | Onde está | Exemplo de valor |
|---|---|---|
| Que **tipo** de entidade participa? | `idTpPapel` → `TipoPapel` | Usuário, Grupo, Sistema |
| Que **papel** a entidade tem na requisição? | `idFrmPapel` → `FormPapel.idPapel` → `Papel.cdPapel` | `ANTE`, `ADO`, `RESP` |
| **Qual** entidade é? | `idPart`, lido conforme o tipo | um usuário, um grupo |

- `idTpPapel` é o **tipo** do participante (chave estrangeira para `TipoPapel`). Os valores estão em [Valores definidos pelo produto](../dominios-do-produto.md).
- O **papel** é lido por `ReqParticipante.idFrmPapel → FormPapel.idPapel → Papel.cdPapel` (chaves estrangeiras). Em `ReqPartConcluida` o caminho é o mesmo, pela coluna `idFrmPapel`.
- O rótulo mostrado na tela pode vir de `FormPapel.dsPapel`, que é o rótulo do papel **naquele formulário**, e pode diferir de `Papel.dsPapel`. A encerrada guarda esse rótulo em `ReqPartConcluida.dsPapel`.
- O par (`idTpPapel`, `idPart`) identifica a entidade participante.

## 2. O que `idPart` aponta, por tipo

| `idTpPapel` | Tipo (`TipoPapel`) | `idPart` aponta para |
|---|---|---|
| `1` | Usuário | `Usuario.idUsu` |
| `2` | Grupo | `Grupo.idGru` |
| `3` | Hierarquia | `OrgHierarquia.idHie` |
| `12` | Grupo de Acesso | `GrupoAcesso.idGru` |
| `8` | Gestor | `Usuario.idUsu` |
| `13` | Externo | `UsuarioExterno.idExt` |

Os tipos `1`, `2`, `3` e `12` estão provados de duas formas: as views de acesso (`vwReqAcessoInterna`) resolvem `idPart` assim (o tipo `3` pela tabela `UsuarioHierarquia`, que usa `idHie`), e a gravação em `Usuario`, `Grupo`, `OrgHierarquia` e `GrupoAcesso` cadastra a entidade em `PartTipoPapel` com o tipo e o próprio id. O tipo `8` (Gestor) está provado pelo código: `CRM_Gestor.idGestor` tem chave estrangeira para `Usuario.idUsu` e a gravação em `CRM_Gestor` cadastra o gestor em `PartTipoPapel` com o tipo `8` e `idGestor`. O tipo `13` está provado pelo código: a gravação em `UsuarioExterno` cadastra o externo como candidato a participante com o tipo `13` e o `idExt`, e o produto liga o participante de tipo `13` ao externo por `ReqParticipante.idPart` = `UsuarioExterno.idExt` ([Pessoa e organização](../dimensoes/pessoa-organizacao.md)). Os demais tipos de `TipoPapel` ficam documentados pelo nome em [Valores definidos pelo produto](../dominios-do-produto.md); o destino de `idPart` deles entra quando for provado.

O papel Solicitante (`ANTE`) pode ser de um usuário (tipo `1`) ou de um externo (tipo `13`); por isso a receita de solicitante usa o tipo `1` de forma explícita.

## 3. Participante vigente

- A tabela guarda o histórico de participações: cada linha tem `dtInicio` e, quando a participação termina, `dtFim`.
- O participante vigente tem `dtFim IS NULL`.
- Quando o atendente muda (por exemplo, no direcionamento), o produto preenche `dtFim` do participante que sai e insere uma nova linha para o que entra.
- `vwParticipante` e `vwPartConcluida` **expõem** `dtFim` e não filtram por ele: o filtro `dtFim IS NULL` é escrito por quem consulta.
- `vwReqAcesso` e `vwReqAcessoConcluida` incluem só participações vigentes: as views internas que as alimentam (`vwReqAcessoInterna` e `vwReqAcessoConcluidaInterna`) aplicam `dtFim IS NULL` em todos os ramos de inclusão, e a coluna `dtFim` não aparece no resultado. A regra de exclusão (seção 5) não consulta `dtFim`.

## 4. Nome exibido do participante

- O nome vem de `PartTipoPapel.nmPart`, com chave primária (`idTpPapel`, `idPart`): uma linha por entidade.
- O caminho recomendado para listar participantes e seus nomes são as tabelas: `ReqParticipante` (ou `ReqPartConcluida`) → `FormPapel` → `Papel`, com `LEFT JOIN PartTipoPapel` pelo par (`idTpPapel`, `idPart`). O `LEFT JOIN` mantém todos os participantes, inclusive os que ainda não têm linha em `PartTipoPapel` (nome vazio).
- Em `ReqPartConcluida`, a coluna `nmPart` guarda o nome da entidade **no momento do encerramento**; ele pode diferir do nome atual em `PartTipoPapel`. Ambos são válidos, para perguntas diferentes: nome na época do encerramento ou nome de hoje.
- Receita pronta: [participantes vigentes](../receitas/participantes-vigentes.md).

## 5. Quem pode ver uma requisição

`vwReqAcessoTotal` junta (`UNION ALL`) `vwReqAcesso` (abertas) e `vwReqAcessoConcluida` (encerradas).

- **Pergunta que responde:** quais usuários têm acesso a uma requisição, ou quais requisições um usuário pode ver.
- **Granularidade:** uma linha por requisição × participante com acesso × usuário. Um grupo participante gera uma linha para cada membro (`flgGrupo` = 1). O mesmo usuário aparece em mais de uma linha da mesma requisição quando participa por mais de um caminho; para listar requisições use `COUNT(DISTINCT idReq)` ou `SELECT DISTINCT idReq`.
- **Cobre:** abertas e encerradas.
- **Como usar:** filtre sempre por `idUsu` ou por `idReq`.
- **O que entra:** os participantes de papel com `FormPapel.flgAcesso = 1`, de tipo Usuário, Gestor, Contato, Grupo, Grupo de Acesso e Hierarquia. As tabelas `QPOQQ` e `QPOQQAcesso` e as views `vwUsuPartQpoqq*` levam a sigla `QPOQQ`, que significa "Quem Pode O Que Quando" (decisão do produto). A regra de exclusão, literal: se a requisição tem alguma participação (vigente ou não) com `FormPapel.flgAcesso = 0`, de tipo `1`, `8`, `7` ou `13`, e com `idPart` igual ao `idUsu` da linha, essa linha de acesso sai. Nos tipos `7` e `13` a comparação é entre `idPart` e `idUsu`.

## Veja também

- [Abertas e encerradas](abertas-e-encerradas.md)
- [Fato: participação](../fatos/participacao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Receita: solicitante e responsável](../receitas/solicitante-e-responsavel.md)
