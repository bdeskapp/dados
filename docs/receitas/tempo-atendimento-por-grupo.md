---
gerado: sincronizacao
---
# Receita: tempo de atendimento por grupo


## 1. Pergunta e indicador

- **Pergunta:** quanto tempo cada grupo ficou com as requisições, abertas e encerradas, abertas num período?
- **Indicador:** tempo de atendimento do grupo = soma, sobre as linhas de atendimento do grupo, de `tAtivoCal + tFreezeCal` (minutos de calendário). A soma separa o tempo em status que conta no SLA (`tAtivoCal`) do tempo em status que não conta (`tFreezeCal`).

## 2. Definição usada

- A linha de atendimento é `ReqTimeAdo` (abertas) ou `ReqTimeAdoConcluida` (encerradas): uma linha por requisição × participação (`idReqPart`) que constava como atendente nos registros de histórico a partir de `dtResposta`. No cálculo dos tempos de requisição com `dtResposta` preenchida, o ADO atual da requisição (participação `ADO` sem `dtFim`) que ainda não tem linha também ganha uma, com os tempos zerados, e essa linha recebe o intervalo do último histórico até o cálculo. Ver [Fato: tempo por grupo](../fatos/tempo-por-grupo.md).
- Essas tabelas não têm `idGru`. O grupo é o `idPart` da participação quando `idTpPapel = 2` (tipo Grupo, ver [Papéis e participação](../mapa/papeis-e-participacao.md)). Participações de outro tipo (por exemplo usuário) não têm grupo e ficam fora do resultado.
- O período filtra por `dtAbertura` da requisição.
- `tAtivoCal + tFreezeCal` de uma requisição soma o `tAtendCal` dela.
- A junção com a participação confere também que a participação é da mesma requisição: em lote, o cálculo de tempos não reinicia a participação atual entre requisições, e uma linha de tempo pode apontar para a participação de outra requisição ([R-tempo-por-grupo-04](../fatos/tempo-por-grupo.md)).
- O tempo anterior à primeira resposta (`tRespCal`) não pertence a nenhuma linha de atendimento e não entra nesta soma.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O primeiro ramo da união é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente.

```sql
SELECT g.idGru, g.dsGru,
       COUNT(DISTINCT x.idReq) AS qtd_requisicoes,
       SUM(CAST(x.tAtivoCal AS bigint)) AS min_ativo_cal,
       SUM(CAST(x.tFreezeCal AS bigint)) AS min_congelado_cal,
       SUM(CAST(x.tAtivoCal AS bigint) + x.tFreezeCal) AS min_atendimento_cal
FROM (
    SELECT a.idReq, rp.idPart AS idGru, a.tAtivoCal, a.tFreezeCal
    FROM ReqTimeAdo a WITH(NOLOCK)
        JOIN ReqParticipante rp WITH(NOLOCK) ON rp.idReqPart = a.idReqPart AND rp.idReq = a.idReq
        JOIN Req r WITH(NOLOCK) ON r.idReq = a.idReq
    WHERE rp.idTpPapel = 2
      AND r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
    UNION ALL
    SELECT a.idReq, rp.idPart, a.tAtivoCal, a.tFreezeCal
    FROM ReqTimeAdoConcluida a WITH(NOLOCK)
        JOIN ReqPartConcluida rp WITH(NOLOCK) ON rp.idReqPart = a.idReqPart AND rp.idReq = a.idReq
        JOIN ReqConcluida c WITH(NOLOCK) ON c.idReq = a.idReq
    WHERE rp.idTpPapel = 2
      AND c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
) x
    JOIN Grupo g WITH(NOLOCK) ON g.idGru = x.idGru
GROUP BY g.idGru, g.dsGru
ORDER BY min_atendimento_cal DESC;
```

Granularidade do resultado: uma linha por grupo. Na parte encerrada, a junção com `ReqPartConcluida` herda o recorte da cópia: a cópia de participantes no encerramento exige cadastro em `PartTipoPapel` e papel ativo no formulário (`FormPapel.flgAtivo = 1`): a participação de quem não tem esse cadastro ou não tem papel ativo no formulário não está em `ReqPartConcluida` e o tempo dela não entra na soma (limite documentado, decisão do produto; ver [Abertas e encerradas](../mapa/abertas-e-encerradas.md), seção 3.1).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idGru | dsGru | qtd_requisicoes | min_ativo_cal | min_congelado_cal | min_atendimento_cal |
    |---|---|---|---|---|---|
    | 9001 | Grupo Exemplo A | 40 | 6000 | 1500 | 7500 |
    | 9002 | Grupo Exemplo B | 12 | 900 | 0 | 900 |

## 5. Regras aplicadas

- [R-tempo-por-grupo-01](../fatos/tempo-por-grupo.md): o grupo vem de `ReqParticipante.idPart` com `idTpPapel = 2`.
- [R-tempo-por-grupo-02](../fatos/tempo-por-grupo.md): some `ReqTimeAdo` e `ReqTimeAdoConcluida` para qualquer histórico.
- [R-tempo-por-grupo-04](../fatos/tempo-por-grupo.md): junte a linha de tempo à participação por `idReqPart` e `idReq`.

## Veja também

- [Fato: tempo por grupo](../fatos/tempo-por-grupo.md)
- [Fato: tempo da requisição](../fatos/tempo-requisicao.md)
- [Receita: tempo total por requisição](tempo-total-por-requisicao.md)
