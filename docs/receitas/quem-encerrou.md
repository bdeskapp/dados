---
gerado: sincronizacao
---
# Receita: quem encerrou a requisição


## 1. Pergunta e indicador

- **Pergunta:** quem executou a ação que levou cada requisição ao seu estado final, e qual foi essa ação?
- **Indicador:** quem encerrou = autor (`idUsu`) do último evento do histórico da requisição encerrada, mostrado junto com o código da ação (`CONC`, `ENC`, `CANC` e assim por diante).

## 2. Definição usada

- A requisição passa para `ReqConcluida` quando chega a um status terminal, isto é, um status sem transição de saída em `FormTransicao`, qualquer que seja a ação. Decisão do produto.
- Quem encerrou é o autor da ação que levou ao status terminal, ou seja, o último evento do histórico antes da passagem para `ReqConcluida`.
- O último evento é o gravado por último: o de maior `idReqHist` da requisição, número que cresce na ordem de gravação, e o que `ReqUltHistConcluida` aponta (`ReqUltHistConcluida.idReqHist`). Ache o último evento por `idReqHist`: `dtFimReqHist` pode ser a data informada numa ação offline, e a ordem por data pode diferir da ordem de gravação.
- `idUsu` vazio é evento sem usuário gravado, que `vwRepUltimaAcao` mostra como "Execução Automática"; o evento do sistema é marcado por `flgSYS` ([R-eventos-historico-02](../fatos/eventos-historico.md)). O período filtra a data de encerramento, `ReqConcluida.dtFimReal`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. Receita só de encerradas: as abertas ainda não têm o evento final.

```sql
SELECT c.idReq, c.dtFimReal, h.idReqHist, h.dtFimReqHist, a.cdAcao, fa.dsAcao, h.idUsu, u.nmUsu
FROM ReqConcluida c WITH(NOLOCK)
    JOIN ReqUltHistConcluida uh WITH(NOLOCK) ON uh.idReq = c.idReq
    JOIN ReqHistConcluida h WITH(NOLOCK) ON h.idReqHist = uh.idReqHist
    LEFT JOIN FormAcao fa WITH(NOLOCK) ON fa.idFrmAcao = h.idFrmAcao
    LEFT JOIN Acao a WITH(NOLOCK) ON a.idAcao = fa.idAcao
    LEFT JOIN Usuario u WITH(NOLOCK) ON u.idUsu = h.idUsu
WHERE c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0;
```

Granularidade do resultado: uma linha por requisição encerrada.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | dtFimReal | cdAcao | dsAcao | idUsu | nmUsu |
    |---|---|---|---|---|---|
    | 5001 | 2030-03-01 10:00 | CONC | Concluir Requisição | 9001 | Usuário Exemplo A |
    | 5002 | 2030-03-02 11:30 | ENC | Encerrar Requisição | | |

## 5. Regras aplicadas

- [R-eventos-historico-02](../fatos/eventos-historico.md): leia o autor do evento em `idUsu`.
- [R-eventos-historico-05](../fatos/eventos-historico.md): o último evento é o de maior `idReqHist`.
- [R-requisicao-01](../fatos/requisicao.md): `ReqConcluida` guarda as encerradas.

## Veja também

- [Fato: eventos do histórico](../fatos/eventos-historico.md)
- [Rejeições de conclusão](rejeicoes-de-conclusao.md)
