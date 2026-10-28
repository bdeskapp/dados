---
gerado: sincronizacao
---
# Receita: taxa de rejeição de conclusão por grupo


## 1. Pergunta e indicador

- **Pergunta:** das requisições encerradas num período, que parte teve a conclusão rejeitada ao menos uma vez, por grupo?
- **Indicador:** taxa de rejeição do grupo = requisições encerradas no período com ao menos um evento `REJCON` ÷ requisições encerradas no período, por grupo atual gravado no encerramento (a consulta devolve a proporção; multiplique por cem para o percentual). A coluna qtd_eventos_rejcon traz também o número de eventos de rejeição, porque uma requisição pode ter mais de uma.

## 2. Definição usada

Decisão do produto: numerador, denominador e grupo como descritos abaixo.

- **Rejeição de conclusão:** cada evento do histórico com a ação `REJCON`, decisão do produto ([R-eventos-historico-04](../fatos/eventos-historico.md)). O código vem de `idFrmAcao → FormAcao.idAcao → Acao.cdAcao` ([R-eventos-historico-01](../fatos/eventos-historico.md)).
- **Numerador:** requisições com ao menos um `REJCON` em qualquer momento do histórico. No encerramento, o histórico passa para `ReqHistConcluida`, então o histórico inteiro da encerrada está nessa tabela ([Fato: eventos do histórico](../fatos/eventos-historico.md), seção 3).
- **Denominador:** requisições encerradas no período de `dtFimReal` ([R-marcos-03](../fatos/marcos.md)), sem as canceladas (status de código `CL`, `FormStatus.idSta` → `Status.cdSta`, [R-status-fase-04](../dimensoes/status-fase.md)), pela mesma regra da receita [SLA por grupo](sla-por-grupo.md). A taxa fica entre 0 e 1, porque o numerador é parte do denominador.
- **Grupo:** o grupo final, o grupo atual gravado na encerrada, `ReqConcluida.idGruAtual`, que guarda o último valor ([R-requisicao-05](../fatos/requisicao.md)). A requisição sem `idGruAtual` (o último solicitado era um usuário) aparece numa linha de grupo vazio.
- **`ReqHistConcluida.idGru` é outra informação:** guarda o grupo do participante em nome do qual o autor do evento agiu, isto é, o `idPart` da participação do evento quando ela é do tipo Grupo, e vazio nos demais tipos. A taxa usa o grupo final `idGruAtual`, decisão do produto.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O status vem do código `FormStatus.idSta` → `Status.cdSta`. A subconsulta `rj` tem uma linha por requisição com `REJCON`, e o `LEFT JOIN` mantém as encerradas sem rejeição. A soma é convertida em `decimal(18,4)` antes da divisão, e a proporção sai com quatro casas decimais (`decimal(9,4)`, arredondada pelo `CAST` externo). Só encerradas, porque o denominador é o encerramento no período.

```sql
SELECT g.idGru, g.dsGru,
       COUNT(*) AS qtd_encerradas,
       SUM(CASE WHEN rj.qtd_rejcon > 0 THEN 1 ELSE 0 END) AS qtd_com_rejeicao,
       ISNULL(SUM(rj.qtd_rejcon), 0) AS qtd_eventos_rejcon,
       CAST(CAST(SUM(CASE WHEN rj.qtd_rejcon > 0 THEN 1 ELSE 0 END) AS decimal(18,4)) / COUNT(*) AS decimal(9,4)) AS taxa_rejeicao
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    LEFT JOIN (
        SELECT h.idReq, COUNT(*) AS qtd_rejcon
        FROM ReqHistConcluida h WITH(NOLOCK)
            JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
            JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
        WHERE a.cdAcao = 'REJCON'
        GROUP BY h.idReq
    ) rj ON rj.idReq = c.idReq
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = c.idGruAtual
WHERE ISNULL(s.cdSta, '') <> 'CL'
  AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
GROUP BY g.idGru, g.dsGru
ORDER BY g.dsGru;
```

Granularidade do resultado: uma linha por grupo atual gravado no encerramento.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idGru | dsGru | qtd_encerradas | qtd_com_rejeicao | qtd_eventos_rejcon | taxa_rejeicao |
    |---|---|---|---|---|---|
    | | | 30 | 0 | 0 | 0.0000 |
    | 1001 | Grupo Exemplo A | 200 | 10 | 12 | 0.0500 |
    | 1002 | Grupo Exemplo B | 80 | 4 | 4 | 0.0500 |

## 5. Regras aplicadas

- [R-eventos-historico-01](../fatos/eventos-historico.md): leia o código da ação por `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- [R-eventos-historico-04](../fatos/eventos-historico.md): conte as rejeições de conclusão pelas ações `REJCON`.
- [R-requisicao-05](../fatos/requisicao.md): o grupo atual é `idGruAtual`; na encerrada, o último valor.
- [R-marcos-03](../fatos/marcos.md): o encerramento é `dtFimReal`, que só existe nas encerradas.
- [R-status-fase-04](../dimensoes/status-fase.md): a cancelada se lê pelo código `CL`.

## Veja também

- [Receita: rejeições de conclusão](rejeicoes-de-conclusao.md)
- [Fato: eventos do histórico](../fatos/eventos-historico.md)
- [Dimensão: ação](../dimensoes/acao.md)
- [Receita: SLA por grupo](sla-por-grupo.md)
