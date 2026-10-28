---
gerado: sincronizacao
---
# Receita: mudanças de grupo


## 1. Pergunta e indicador

- **Pergunta:** quantas vezes uma requisição foi direcionada, e quantos direcionamentos tiveram as requisições de cada grupo?
- **Indicador:** mudanças de grupo = número de eventos de histórico com a ação `DIR` (direcionar), somando abertas e encerradas. A ação `DIR` direciona para um grupo ou para um usuário, e as trocas de grupo por devolução ou por recategorização não entram na contagem.

## 2. Definição usada

- Uma mudança de grupo é cada evento do histórico cuja ação é `DIR`, direcionamento para grupo ou para usuário (decisão do produto). Trocas de grupo por devolução ou por recategorização ficam fora. O código vem de `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- O período filtra a data do evento, `dtFimReqHist`.
- "Por grupo" agrupa pelo grupo final da requisição, o grupo atual (`idGruAtual`, ver [Fato: requisição](../fatos/requisicao.md)): conta os direcionamentos das requisições que estão hoje (ou estavam, no encerramento) com aquele grupo (decisão do produto). A coluna `ReqHistorico.idGru` fica fora desta receita.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. Cada bloco soma o ramo das abertas (`ReqHistorico`) e o das encerradas (`ReqHistConcluida`); para um estado só, mantenha o ramo correspondente.

Por requisição, uma linha por requisição com ao menos um direcionamento:

```sql
SELECT x.idReq, COUNT(*) AS qtd_direcionamentos, MIN(x.dtFimReqHist) AS primeiro, MAX(x.dtFimReqHist) AS ultimo
FROM (
    SELECT h.idReq, h.dtFimReqHist
    FROM ReqHistorico h WITH(NOLOCK)
        JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
        JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    WHERE a.cdAcao = 'DIR'
        AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0
    UNION ALL
    SELECT h.idReq, h.dtFimReqHist
    FROM ReqHistConcluida h WITH(NOLOCK)
        JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
        JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    WHERE a.cdAcao = 'DIR'
        AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0
) x
GROUP BY x.idReq;
```

Granularidade do resultado: uma linha por requisição.

Por grupo atual, uma linha por grupo (a linha sem grupo reúne as requisições sem `idGruAtual`):

```sql
SELECT g.idGru, g.dsGru, COUNT(*) AS qtd_direcionamentos, COUNT(DISTINCT x.idReq) AS qtd_requisicoes
FROM (
    SELECT h.idReq, r.idGruAtual
    FROM ReqHistorico h WITH(NOLOCK)
        JOIN Req r WITH(NOLOCK) ON r.idReq = h.idReq
        JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
        JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    WHERE a.cdAcao = 'DIR'
        AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0
    UNION ALL
    SELECT h.idReq, r.idGruAtual
    FROM ReqHistConcluida h WITH(NOLOCK)
        JOIN ReqConcluida r WITH(NOLOCK) ON r.idReq = h.idReq
        JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
        JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    WHERE a.cdAcao = 'DIR'
        AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0
) x
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = x.idGruAtual
GROUP BY g.idGru, g.dsGru;
```

Granularidade do resultado: uma linha por grupo atual.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    **exemplo fictício** (por grupo)

    | idGru | dsGru | qtd_direcionamentos | qtd_requisicoes |
    |---|---|---|---|
    | 9001 | Grupo Exemplo A | 12 | 9 |
    | 9002 | Grupo Exemplo B | 5 | 4 |

## 5. Regras aplicadas

- [R-eventos-historico-01](../fatos/eventos-historico.md): leia o código da ação por `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- [R-eventos-historico-04](../fatos/eventos-historico.md): conte direcionamentos pelas ações `DIR`.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas.

## Veja também

- [Fato: eventos do histórico](../fatos/eventos-historico.md)
- [Fato: requisição](../fatos/requisicao.md)
