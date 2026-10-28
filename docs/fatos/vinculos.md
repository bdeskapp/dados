---
gerado: sincronizacao
---
# Fato: vínculos entre requisições


## 1. O que mede

Quais requisições nasceram de outra (etapas de um processo e desdobramentos) e quais se referenciam ou dependem de outra. Serve para listar as filhas de uma requisição, subir da filha ao pai e medir a profundidade de um fluxo.

## 2. Granularidade

- `ReqVinculada`: uma linha por par (`idReq` = pai, `idReqVinculo` = filha). O par é único.
- `ReqVinculadaRef`: uma linha por par de referência, dependência ou desdobramento com dependência; aqui `idReq` é a requisição que referencia e `idReqVinculo` a referenciada.

## 3. Tabelas

| Tabela | Conteúdo | Observação |
|---|---|---|
| `ReqVinculada` | árvore pai → filha | uma só tabela para abertas e encerradas |
| `ReqVinculadaRef` | referências, dependências e desdobramentos com dependência | uma só tabela para abertas e encerradas |
| `Vinculo` | código e descrição do vínculo (`cdVinc`, `dsVinc`) | |
| `TipoVinculo` | tipo do vínculo (`idTpVinculo`, `cdTpVinculo`, `dsTpVinculo`) | `TipoVinculo.cdTpVinculo` aponta para `Vinculo.cdVinc`; o produto grava e compara os códigos `DESD`, `DESDD`, `REF` e `DEP`; os valores de `ReqVinculada.idTpVinculo`, `ReqVinculada.cdVinc` e `ReqVinculadaRef.cdVinc` que o produto define estão em [Valores definidos pelo produto](../dominios-do-produto.md), sem rótulo; `cdVinc` também pode vir vazio, porque a abertura de etapa de processo e o vínculo automático não o informam |

- **Sem par aberta/encerrada.** As duas tabelas de vínculo não têm versão "Concluida": a linha continua onde está quando a requisição é encerrada. O pai e a filha de um mesmo vínculo podem estar, cada um, em `Req` ou em `ReqConcluida`; para trazer dados da requisição use `LEFT JOIN` nas duas tabelas (ver a receita [filhas de um pai](../receitas/filhas-de-um-pai.md)).
- **Quem grava.** O produto. A abertura de uma etapa de processo grava `ReqVinculada` com `idTpVinculo` 7: `idReqVinculo` é a etapa aberta e `idReq` é a requisição que a originou, ou a centralizadora do fluxo pai quando a requisição de origem está em outro fluxo; o valor 7 é fixo nessa gravação, que não informa `cdVinc`; para identificar as etapas de processo, filtre `ReqVinculada.idTpVinculo = 7` (o valor 7 não tem rótulo no produto; esta página o descreve pelo comportamento do produto, e `cdVinc` dessas linhas fica vazio: nada grava `cdVinc` `FLU`, a coluna é `CHAR(5) NULL` sem valor padrão, e o produto apenas exclui `FLU` das consultas). O desdobramento grava `ReqVinculada` com `cdVinc` `DESD`. Referência e dependência gravam `ReqVinculadaRef` com `cdVinc` `REF` e `DEP`; o desdobramento com dependência grava nela `DESDD` e não grava `ReqVinculada`: `idReq` recebe a requisição desdobrada e `idReqVinculo` recebe a original. Há ainda um vínculo automático gravado em `ReqVinculadaRef` sem `cdVinc` nem `idTpVinculo`.
- `cdVinc` é `CHAR(5)`: leia com `RTRIM(cdVinc)`.

## 4. Colunas-chave

| Coluna | Significado | Unidade |
|---|---|---|
| `ReqVinculada.idReq` | requisição pai | |
| `ReqVinculada.idReqVinculo` | requisição filha | |
| `ReqVinculada.idTpVinculo` | tipo do vínculo (`TipoVinculo`) | |
| `ReqVinculada.cdVinc` | código do vínculo (`Vinculo.cdVinc`); pode vir vazio | texto de 5 posições |
| `ReqVinculada.idFlu` | fluxo ao qual o vínculo pertence | |
| `ReqVinculada.nivel` | nível da filha dentro do fluxo: o maior nível do pai no fluxo mais um | |
| `ReqVinculadaRef.tpConc` | andamento da dependência (pendente, concluída, cancelada, encerrada) | código |

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição pai | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Requisição filha | `idReqVinculo` → `Req.idReq` ou `ReqConcluida.idReq` |
| Fluxo | `idFlu` → `Workflow.idFlu` (ver a seção "Fluxo" em [Fato: requisição](requisicao.md)) |
| Vínculo | `cdVinc` → `Vinculo.cdVinc`; `idTpVinculo` → `TipoVinculo.idTpVinculo` |

## 6. Regras de uso

#### R-vinculos-01: Ache as filhas de um pai em `ReqVinculada` (`idReq` = pai) e em `ReqVinculadaRef` com `cdVinc` `DESDD` (`idReqVinculo` = pai). {#r-vinculos-01}
Em `ReqVinculada`, `idReq` é o pai e `idReqVinculo` a filha: para as filhas de um pai filtre `idReq`; para o pai de uma filha filtre `idReqVinculo`. O desdobramento com dependência (`DESDD`) fica só em `ReqVinculadaRef`, no sentido inverso: `idReq` é a filha desdobrada e `idReqVinculo` a original. Para reunir todas as filhas, una as linhas de `ReqVinculada` com `idReq` = pai às linhas de `ReqVinculadaRef` com `RTRIM(cdVinc)` = `DESDD` e `idReqVinculo` = pai (a filha é `idReq` nessas linhas).
Receita: [filhas de um pai](../receitas/filhas-de-um-pai.md)

#### R-vinculos-02: Resolva o estado de pai e filha com `LEFT JOIN` em `Req` e em `ReqConcluida`. {#r-vinculos-02}
`ReqVinculada` serve a abertas e encerradas e não tem versão encerrada; cada ponta do par está em uma das duas tabelas de requisição.
Receita: [filhas de um pai](../receitas/filhas-de-um-pai.md)

#### R-vinculos-03: Leia o código do vínculo com `RTRIM(cdVinc)`, e o tipo em `idTpVinculo`. {#r-vinculos-03}
`cdVinc` é `CHAR(5)` e pode vir vazio; `idTpVinculo` está sempre preenchido em `ReqVinculada`. Nenhuma rotina do produto grava `cdVinc` `FLU`: um `FLU` que apareça em `cdVinc` é dado legado. Para a etapa de processo, filtre `idTpVinculo = 7`, valor que o produto grava ao abrir uma etapa, e para o desdobramento sem dependência filtre `cdVinc` `DESD`; esses valores não têm rótulo no produto ([Valores definidos pelo produto](../dominios-do-produto.md)). Os códigos que o produto grava e compara são `DESD`, `DESDD`, `REF` e `DEP`; `TipoVinculo.cdTpVinculo` aponta para `Vinculo.cdVinc`.
Receita: [filhas de um pai](../receitas/filhas-de-um-pai.md)

#### R-vinculos-04: Leia o sentido de `ReqVinculadaRef` pelo código do vínculo. {#r-vinculos-04}
- `REF`: `idReq` é a requisição que referencia e `idReqVinculo` a referenciada; o produto confere a existência do par nos dois sentidos antes de gravar.
- `DEP`: `idReq` é a requisição principal e `idReqVinculo` a secundária, que recebe `flgDepende`.
- `DESDD`: `idReq` é a requisição desdobrada e `idReqVinculo` a original.

É o sentido oposto ao de `ReqVinculada`, em que `idReq` é o pai.

## 7. Views recomendadas

Nenhuma. As duas tabelas respondem direto às perguntas desta página.

## 8. Receitas

- [Filhas de um pai](../receitas/filhas-de-um-pai.md)

## Veja também

- [Fato: requisição](requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
