---
gerado: sincronizacao
---
# Receita: último atendente das requisições abertas


## 1. Pergunta e indicador

- **Pergunta:** em cada requisição aberta, quem foi o último atendente a registrar algo, e quando?
- **Indicador:** último atendente = autor (`idUsu`) do último evento do histórico registrado sob uma participação de papel de atendimento (`ADO`, `RESP`, `APROV`, `SHADO`, `SAN`, `SHANTE`).

## 2. Definição usada

Decisão do produto: atendente é quem registra evento sob participação de papel de atendimento da lista do produto, sem os eventos executados pelo sistema.

- **Papel de atendimento:** a mesma lista que o produto usa para gravar `dtResposta` e `dtUltHistADO` no registro de histórico: `ADO`, `RESP`, `APROV`, `SHADO`, `SAN` e `SHANTE`. O produto compara o papel da participação sob a qual o evento foi registrado (`ReqHistorico.idReqPart`). A receita lê esse papel por `idReqPart → ReqParticipante.idFrmPapel → FormPapel.idPapel → Papel.cdPapel` ([R-participacao-01](../fatos/participacao.md)).
- **Eventos do sistema ficam fora pelo filtro `flgSYS = 0`.** O registro de histórico grava o valor de `flgSYS` na coluna `ReqHistorico.flgSYS`; com `flgSYS = 1`, o evento é registrado sob a participação de tipo `11` (Sistema) da requisição. O evento recebido por e-mail, registrado sob a participação de tipo E-mail ([R-eventos-historico-02](../fatos/eventos-historico.md)), fica fora pelo papel: essa participação tem o papel `EMAIL`, que não está na lista.
- **Último:** o de maior `idReqHist`. `ReqHistorico.idReqHist` é `IDENTITY(1, 1)` e chave primária: cada evento tem um número próprio, e o maior é o último registrado. É o mesmo critério de `dtUltHistADO` nos eventos de atendimento gravados no histórico, e o registro de histórico atualiza essa coluna com o `dtFimReqHist` de cada evento de atendimento, sem comparar datas ([Marcos](../fatos/marcos.md)); a ação `CAT` também conta, como em `dtUltHistADO`. A coluna só é atualizada quando o evento de abertura é registrado sob um papel de atendimento (`ADO`, `RESP`, `APROV`, `SHADO`, `SAN` ou `SHANTE`); sob outro papel, a abertura mantém a coluna como está. Para o último por data, ordene por `dtFimReqHist` e desempate por `dtRegistro` ([R-eventos-historico-03](../fatos/eventos-historico.md)).
- **A receita lê o histórico, não a coluna `dtUltHistADO`.** `Req.dtUltHistADO` pode divergir da data do evento escolhido; o produto grava a coluna com o `dtFimReqHist` do evento sem comparar datas.
- **Autor e participação:** o autor é `idUsu` ([R-eventos-historico-02](../fatos/eventos-historico.md)), com o nome por `LEFT JOIN Usuario`. `idTpPapel` e `idPart` dizem sob que participação ele agiu: tipo `1` (Usuário) com `idPart` igual ao `idUsu`, ou tipo `2` (Grupo) com `idPart` → `Grupo.idGru` ([R-participacao-03](../fatos/participacao.md)).
- **Todas as abertas aparecem.** A consulta parte de `Req` com `LEFT JOIN`; a aberta sem evento de atendimento sai com as colunas do evento vazias e sem_atendimento = 1.

## 3. SQL

Compatível com SQL Server em nível 130; sem parâmetros; `WITH(NOLOCK)`. Só abertas: `Req`, `ReqHistorico` e `ReqParticipante` guardam as requisições em andamento. A subconsulta `ua` numera, por requisição, os eventos de atendimento que não foram executados pelo sistema, do maior `idReqHist` para o menor, e o `JOIN` pega o primeiro.

```sql
SELECT r.idReq, ua.idReqHist, ua.dtFimReqHist, ua.cdPapel, ua.idTpPapel, ua.idPart,
       ua.idUsu, u.nmUsu,
       CASE WHEN ua.idReqHist IS NULL THEN 1 ELSE 0 END AS sem_atendimento
FROM Req r WITH(NOLOCK)
    LEFT JOIN (
        SELECT h.idReq, h.idReqHist, h.dtFimReqHist, h.idUsu, p.cdPapel, rp.idTpPapel, rp.idPart,
               ROW_NUMBER() OVER (PARTITION BY h.idReq ORDER BY h.idReqHist DESC) AS ordem
        FROM ReqHistorico h WITH(NOLOCK)
            JOIN ReqParticipante rp WITH(NOLOCK) ON rp.idReqPart = h.idReqPart
            JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
            JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
        WHERE p.cdPapel IN ('ADO', 'RESP', 'APROV', 'SHADO', 'SAN', 'SHANTE')
          AND h.flgSYS = 0
    ) ua ON ua.idReq = r.idReq AND ua.ordem = 1
    LEFT JOIN Usuario u WITH(NOLOCK) ON u.idUsu = ua.idUsu;
```

Granularidade do resultado: uma linha por requisição aberta.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | idReqHist | dtFimReqHist | cdPapel | idTpPapel | idPart | idUsu | nmUsu | sem_atendimento |
    |---|---|---|---|---|---|---|---|---|
    | 1001 | 7001 | 2030-03-01 10:00 | ADO | 2 | 1101 | 1201 | Usuário Exemplo A | 0 |
    | 1002 | 7002 | 2030-03-02 14:30 | RESP | 1 | 1202 | 1202 | Usuário Exemplo B | 0 |
    | 1003 | | | | | | | | 1 |

## 5. Regras aplicadas

- [R-participacao-01](../fatos/participacao.md): leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- [R-participacao-03](../fatos/participacao.md): leia `idPart` conforme o tipo.
- [R-eventos-historico-02](../fatos/eventos-historico.md): o autor do evento é `idUsu`; `idReqPart` é a participação sob a qual o evento foi registrado.
- [R-eventos-historico-03](../fatos/eventos-historico.md): a data do evento é `dtFimReqHist`; `dtRegistro` desempata eventos da mesma data.
- [R-marcos-01](../fatos/marcos.md): `dtResposta` usa a mesma lista de papéis de atendimento.

## Veja também

- [Fato: eventos do histórico](../fatos/eventos-historico.md)
- [Fato: participação](../fatos/participacao.md)
- [Marcos da requisição](../fatos/marcos.md)
- [Receita: quem encerrou](quem-encerrou.md)
