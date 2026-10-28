---
gerado: sincronizacao
---
# Receita: tempo em cada status


## 1. Pergunta e indicador

- **Pergunta:** quanto tempo as requisições, abertas e encerradas, abertas num período, passaram em cada status?
- **Indicador:** tempo no status = soma de `nIntervaloCal` (minutos de calendário) e de `nIntervaloReal` (minutos corridos) das passagens por aquele status, e a média por passagem.

## 2. Definição usada

- Uma linha de `ReqStatus` (aberta) ou `ReqStatusConcluida` (encerrada) é uma passagem da requisição por um status, de `dtIniStatus` a `dtFimStatus`. O mesmo status pode aparecer mais de uma vez na mesma requisição; a receita exclui as passagens de intervalo negativo (`nIntervaloReal` ou `nIntervaloCal` menor que 0, o que acontece com datas fora da ordem) e mantém as demais, inclusive as de intervalo vazio (decisão do produto: no tempo por status, excluir só os intervalos negativos) ([Fato: tempo por status](../fatos/tempo-por-status.md)).
- O status é lido pelo código: `FormStatus.idSta` → `Status.cdSta`. O rótulo `FormStatus.dsSta` é do formulário e pode diferir entre formulários.
- A passagem atual de uma aberta pode ter `dtFimStatus` e intervalos vazios, ou o valor provisório da última atualização em lote; `SUM` e `AVG` ignoram os vazios, e a coluna qtd_passagens conta a passagem.
- O período filtra por `dtAbertura` da requisição.
- `ReqStatus` é uma fonte própria e não se soma com os tempos de `ReqTime`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. O primeiro ramo da união é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente.

```sql
SELECT x.cdSta,
       COUNT(*) AS qtd_passagens,
       COUNT(DISTINCT x.idReq) AS qtd_requisicoes,
       SUM(CAST(x.nIntervaloCal AS bigint)) AS min_calendario,
       SUM(CAST(x.nIntervaloReal AS bigint)) AS min_relogio,
       AVG(CAST(x.nIntervaloCal AS float)) AS media_min_calendario
FROM (
    SELECT rs.idReq, s.cdSta, rs.nIntervaloCal, rs.nIntervaloReal
    FROM ReqStatus rs WITH(NOLOCK)
        JOIN Req r WITH(NOLOCK) ON r.idReq = rs.idReq
        JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = rs.idFrmStatus
        JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
      AND ISNULL(rs.nIntervaloReal, 0) >= 0 AND ISNULL(rs.nIntervaloCal, 0) >= 0
    UNION ALL
    SELECT rs.idReq, s.cdSta, rs.nIntervaloCal, rs.nIntervaloReal
    FROM ReqStatusConcluida rs WITH(NOLOCK)
        JOIN ReqConcluida c WITH(NOLOCK) ON c.idReq = rs.idReq
        JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = rs.idFrmStatus
        JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    WHERE c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
      AND ISNULL(rs.nIntervaloReal, 0) >= 0 AND ISNULL(rs.nIntervaloCal, 0) >= 0
) x
GROUP BY x.cdSta
ORDER BY x.cdSta;
```

Granularidade do resultado: uma linha por código de status.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | cdSta | qtd_passagens | qtd_requisicoes | min_calendario | min_relogio | media_min_calendario |
    |---|---|---|---|---|---|
    | AB | 100 | 100 | 20000 | 60000 | 200 |
    | EA | 140 | 90 | 28000 | 70000 | 200 |

## 5. Regras aplicadas

- [R-tempo-por-status-01](../fatos/tempo-por-status.md): some `ReqStatus` e `ReqStatusConcluida`.
- [R-tempo-por-status-02](../fatos/tempo-por-status.md): conte passagens por linha e requisições por `COUNT(DISTINCT idReq)`.
- [R-tempo-por-status-03](../fatos/tempo-por-status.md): leia o status por `FormStatus.idSta` → `Status.cdSta`.

## Veja também

- [Fato: tempo por status](../fatos/tempo-por-status.md)
- [Fato: tempo da requisição](../fatos/tempo-requisicao.md)
