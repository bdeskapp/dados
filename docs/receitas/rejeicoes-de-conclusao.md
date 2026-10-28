---
gerado: sincronizacao
---
# Receita: rejeições de conclusão


## 1. Pergunta e indicador

- **Pergunta:** quais requisições tiveram a conclusão rejeitada, quando e por quem?
- **Indicador:** rejeições de conclusão = número de eventos de histórico com a ação `REJCON` (rejeitar conclusão). As colunas `encerrada` e ultimo_evento marcam a rejeição de conclusão que ficou como último evento registrado de uma requisição encerrada.

## 2. Definição usada

- Cada evento do histórico com a ação `REJCON` é uma rejeição de conclusão; a receita a conta sem exigir uma ação `CONC` anterior. A contagem pelas ações `REJCON` é a decisão do produto.
- A rejeição de conclusão nem sempre devolve a requisição ao atendimento. O próximo status vem de `FormTransicao` (ação + status atual), e um formulário pode levar `REJCON` a um status terminal, sem transição de saída; nesse caso o produto encerra a requisição no status resultante ([Status](../dimensoes/status-fase.md), seção 5).
- ultimo_evento vale `1` quando o `REJCON` é o último evento registrado da requisição, isto é, o `idReqHist` de `ReqUltHist` (abertas) ou de `ReqUltHistConcluida` (encerradas) ([R-eventos-historico-05](../fatos/eventos-historico.md), [R-eventos-historico-06](../fatos/eventos-historico.md)). Numa encerrada, ultimo_evento igual a 1 quer dizer que a requisição ficou encerrada sem outro evento registrado depois da rejeição; numa aberta, que a rejeição é o evento mais recente até o momento da consulta. O filtro de `encerrada` igual a 1 e ultimo_evento igual a 1 aproxima as rejeições de conclusão que encerraram a requisição: deixa de fora a rejeição que levou a requisição ao status terminal quando outro evento ficou registrado depois dela, antes da passagem para `ReqConcluida` (o último evento de uma encerrada nem sempre é a ação cuja transição leva ao status final).
- Uma requisição pode ter mais de uma rejeição; o resultado tem uma linha por evento. Para contar rejeições por requisição, agrupe por `idReq`.
- O período filtra `dtFimReqHist`. O autor vem de `idUsu`, ligado a `Usuario` por `LEFT JOIN`; `idUsu` vazio é evento sem usuário gravado, e o evento automático do sistema se lê por `flgSYS` ([R-eventos-historico-02](../fatos/eventos-historico.md)).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O primeiro ramo é o das abertas e o segundo o das encerradas; a coluna `encerrada` vale `0` nas abertas e `1` nas encerradas. Para um estado só, mantenha o ramo correspondente.

```sql
SELECT h.idReq, h.idReqHist, h.dtFimReqHist, h.idUsu, u.nmUsu, 0 AS encerrada,
    CASE WHEN uh.idReqHist IS NOT NULL THEN 1 ELSE 0 END AS ultimo_evento
FROM ReqHistorico h WITH(NOLOCK)
    JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
    JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    LEFT JOIN Usuario u WITH(NOLOCK) ON u.idUsu = h.idUsu
    LEFT JOIN ReqUltHist uh WITH(NOLOCK) ON uh.idReq = h.idReq AND uh.idReqHist = h.idReqHist
WHERE a.cdAcao = 'REJCON'
    AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0
UNION ALL
SELECT h.idReq, h.idReqHist, h.dtFimReqHist, h.idUsu, u.nmUsu, 1,
    CASE WHEN uh.idReqHist IS NOT NULL THEN 1 ELSE 0 END
FROM ReqHistConcluida h WITH(NOLOCK)
    JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
    JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    LEFT JOIN Usuario u WITH(NOLOCK) ON u.idUsu = h.idUsu
    LEFT JOIN ReqUltHistConcluida uh WITH(NOLOCK) ON uh.idReq = h.idReq AND uh.idReqHist = h.idReqHist
WHERE a.cdAcao = 'REJCON'
    AND h.dtFimReqHist >= /* @dtInicio */ 0 AND h.dtFimReqHist < /* @dtFim */ 0;
```

Granularidade do resultado: uma linha por evento de rejeição (`idReqHist`).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | idReqHist | dtFimReqHist | idUsu | nmUsu | encerrada | ultimo_evento |
    |---|---|---|---|---|---|---|
    | 5001 | 70001 | 2030-03-01 10:00 | 9001 | Usuário Exemplo A | 0 | 1 |
    | 5002 | 70002 | 2030-03-02 11:30 | 9002 | Usuário Exemplo B | 1 | 0 |
    | 5003 | 70003 | 2030-03-03 09:15 | 9001 | Usuário Exemplo A | 1 | 1 |

## 5. Regras aplicadas

- [R-eventos-historico-01](../fatos/eventos-historico.md): leia o código da ação por `idFrmAcao → FormAcao.idAcao → Acao.cdAcao`.
- [R-eventos-historico-03](../fatos/eventos-historico.md): leia a data do evento em `dtFimReqHist`.
- [R-eventos-historico-04](../fatos/eventos-historico.md): conte as rejeições de conclusão pelas ações `REJCON`; aqui as colunas `encerrada` e ultimo_evento marcam as que ficaram como último evento da encerrada.
- [R-eventos-historico-05](../fatos/eventos-historico.md): o último evento registrado de uma encerrada é o de `ReqUltHistConcluida`.
- [R-eventos-historico-06](../fatos/eventos-historico.md): a última ação está em `ReqUltHist` (abertas) e `ReqUltHistConcluida` (encerradas).

## Veja também

- [Fato: eventos do histórico](../fatos/eventos-historico.md)
- [Quem encerrou](quem-encerrou.md)
