---
gerado: sincronizacao
---
# Receita: requisições atrasadas agora


## 1. Pergunta e indicador

- **Pergunta:** que requisições abertas de um grupo já passaram do prazo neste momento, e há quanto tempo?
- **Indicador:** atraso da requisição = minutos corridos entre `dtFimPrev` e o momento da consulta, para as abertas cujo `dtFimPrev` é anterior a esse momento.

## 2. Definição usada

Decisão do produto:

- **Atrasada agora:** requisição aberta com `dtFimPrev` anterior ao momento da consulta.
- Entram as requisições em status que não conta no SLA (`FormStatus.flgContaSLA = 0`). As colunas `cdSta` (código do status, `FormStatus.idSta` → `Status.cdSta`) e `flgContaSLA` acompanham cada linha para quem quiser separá-las; as duas saem vazias quando a requisição não tem status (`Req.idFrmStatus` aceita `NULL`), e a linha continua na lista.
- O grupo é o grupo atual (`idGruAtual`).
- A conta lê a data prevista; a flag `Req.flgForaSLA` é gravada pelo plano de alertas, onde retrata o último evento dele, e regravada com 0 por uma atualização de versão do produto ([Prioridade e SLA](../dimensoes/prioridade-sla.md)).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro como placeholder fictício; `WITH(NOLOCK)`. Só abertas, porque `dtFimReal` das encerradas já fecha o prazo.

```sql
SELECT r.idReq, r.dtFimPrev,
       DATEDIFF(mi, r.dtFimPrev, GETDATE()) AS min_atraso_relogio,
       r.idGruAtual, g.dsGru, s.cdSta, fs.flgContaSLA
FROM Req r WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = r.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = r.idGruAtual
WHERE r.idGruAtual = /* @idGru */ 0
  AND r.dtFimPrev < GETDATE()
ORDER BY r.dtFimPrev;
```

Granularidade do resultado: uma linha por requisição.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | dtFimPrev | min_atraso_relogio | idGruAtual | dsGru | cdSta | flgContaSLA |
    |---|---|---|---|---|---|---|
    | 2001 | 2030-03-01 | 4320 | 9001 | Grupo Exemplo A | EA | 1 |
    | 2002 | 2030-03-02 | 1440 | 9001 | Grupo Exemplo A | PN | 0 |

## 5. Regras aplicadas

- [R-marcos-02](../fatos/marcos.md): "estourou o prazo" compara `dtFimPrev` com o momento da consulta nas abertas.
- [R-marcos-04](../fatos/marcos.md): leia o prazo pelas datas; `flgForaSLA` é gravada pelo plano de alertas e regravada com 0 por uma atualização de versão do produto.
- [R-requisicao-05](../fatos/requisicao.md): o grupo atual é `idGruAtual`.

## Veja também

- [Receita: SLA por grupo](sla-por-grupo.md)
- [Marcos da requisição](../fatos/marcos.md)
