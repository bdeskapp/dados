---
gerado: sincronizacao
---
# Receita: fora do SLA por prioridade


## 1. Pergunta e indicador

- **Pergunta:** quantas requisições de cada prioridade foram encerradas fora do prazo num período, e quantas das abertas já estão fora do prazo agora?
- **Indicador:** fora do SLA da prioridade = requisições fora do prazo ÷ requisições consideradas (a consulta devolve as duas contagens e a proporção; multiplique por cem para o percentual), por `nPrioridade`. Nas encerradas, "fora do prazo" é `dtFimReal` posterior a `dtFimPrev`; nas abertas, é `dtFimPrev` anterior ao momento da consulta.

## 2. Definição usada

- **Fora do prazo pelas datas previstas** ([R-prioridade-sla-03](../dimensoes/prioridade-sla.md)), na decisão do produto ([R-marcos-02](../fatos/marcos.md)): estourou o prazo é `dtFimPrev` anterior a `dtFimReal` (encerradas) ou ao momento da consulta (abertas). A conta lê as datas; a flag `flgForaSLA` é gravada pelo plano de alertas, onde retrata o último evento dele, e regravada com 0 por uma atualização de versão do produto ([R-marcos-04](../fatos/marcos.md)). A receita usa o mesmo conjunto de requisições e as mesmas comparações de [SLA por grupo](sla-por-grupo.md), e cada requisição considerada cai numa só das duas contagens: no prazo naquela receita ou fora do prazo nesta. O complemento vale por requisição e no total do período; linha a linha as duas receitas não se casam, porque uma agrupa por grupo e a outra por prioridade.
- **Canceladas ficam fora do denominador,** pela definição do SLA decisão do produto ([SLA por grupo](sla-por-grupo.md)): a receita descarta o status de código `CL` (`FormStatus.idSta` → `Status.cdSta`, [R-status-fase-04](../dimensoes/status-fase.md)).
- **Prioridade:** o número gravado em `nPrioridade` ([R-prioridade-sla-02](../dimensoes/prioridade-sla.md)), `tinyint` sem chave estrangeira, presente em `Req` e em `ReqConcluida`. A receita agrupa pelo número; o rótulo de cada número (`1` Alta, `2` Média, `3` Baixa) está em [Valores definidos pelo produto](../dominios-do-produto.md), seção `Req.nPrioridade` ([Prioridade e SLA](../dimensoes/prioridade-sla.md), seção 5).
- **Encerradas:** entram pelo período de `dtFimReal`, que só existe nelas ([R-marcos-03](../fatos/marcos.md)).
- **Abertas:** entram todas, exceto as canceladas, no momento da consulta; a consulta das abertas não tem filtro de data. Cada aberta conta com o `dtFimPrev` gravado hoje.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta das encerradas devolve vazio (a das abertas não tem filtro de data). O status vem do código `FormStatus.idSta` → `Status.cdSta`. A soma é convertida em `decimal(18,4)` antes da divisão, e a proporção sai com quatro casas decimais (`decimal(9,4)`, arredondada pelo `CAST` externo).

Encerradas no período:

```sql
SELECT c.nPrioridade,
       COUNT(*) AS qtd_encerradas,
       SUM(CASE WHEN c.dtFimReal > c.dtFimPrev THEN 1 ELSE 0 END) AS qtd_fora_do_prazo,
       CAST(CAST(SUM(CASE WHEN c.dtFimReal > c.dtFimPrev THEN 1 ELSE 0 END) AS decimal(18,4)) / COUNT(*) AS decimal(9,4)) AS proporcao_fora_do_prazo
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
WHERE ISNULL(s.cdSta, '') <> 'CL'
  AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
GROUP BY c.nPrioridade
ORDER BY c.nPrioridade;
```

Granularidade do resultado: uma linha por valor de `nPrioridade`.

Abertas, no momento da consulta:

```sql
SELECT r.nPrioridade,
       COUNT(*) AS qtd_abertas,
       SUM(CASE WHEN r.dtFimPrev < GETDATE() THEN 1 ELSE 0 END) AS qtd_fora_do_prazo,
       CAST(CAST(SUM(CASE WHEN r.dtFimPrev < GETDATE() THEN 1 ELSE 0 END) AS decimal(18,4)) / COUNT(*) AS decimal(9,4)) AS proporcao_fora_do_prazo
FROM Req r WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = r.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
WHERE ISNULL(s.cdSta, '') <> 'CL'
GROUP BY r.nPrioridade
ORDER BY r.nPrioridade;
```

Granularidade do resultado: uma linha por valor de `nPrioridade`.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    **exemplo fictício** (encerradas)

    | nPrioridade | qtd_encerradas | qtd_fora_do_prazo | proporcao_fora_do_prazo |
    |---|---|---|---|
    | 1 | 50 | 5 | 0.1000 |
    | 2 | 200 | 30 | 0.1500 |
    | 3 | 20 | 8 | 0.4000 |

## 5. Regras aplicadas

- [R-prioridade-sla-03](../dimensoes/prioridade-sla.md): "estourou o prazo" se mede pelas datas previstas.
- [R-prioridade-sla-02](../dimensoes/prioridade-sla.md): `nPrioridade` é número sem chave estrangeira.
- [R-marcos-02](../fatos/marcos.md): compare `dtFimPrev` com `dtFimReal` (encerradas) ou com o momento da consulta (abertas).
- [R-marcos-03](../fatos/marcos.md): `dtFimReal` só existe nas encerradas.
- [R-marcos-04](../fatos/marcos.md): `flgForaSLA` é gravada pelo plano de alertas e regravada com 0 por uma atualização de versão do produto; a conta lê as datas.
- [R-status-fase-04](../dimensoes/status-fase.md): a cancelada se lê pelo código `CL`.

## Veja também

- [Dimensão: prioridade e SLA](../dimensoes/prioridade-sla.md)
- [Marcos da requisição](../fatos/marcos.md)
- [Receita: SLA por grupo](sla-por-grupo.md)
- [Receita: atrasadas agora](atrasadas-agora.md)
