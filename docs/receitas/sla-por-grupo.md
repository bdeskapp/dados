---
gerado: sincronizacao
---
# Receita: percentual dentro do SLA por grupo


## 1. Pergunta e indicador

- **Pergunta:** que percentual das requisições de cada grupo foi encerrado dentro do prazo, e que percentual das abertas ainda está dentro do prazo agora?
- **Indicador:** % dentro do SLA do grupo = requisições no prazo ÷ requisições consideradas (a consulta devolve a proporção; multiplique por cem para o percentual), por grupo atual. Nas encerradas, "no prazo" é `dtFimReal` igual ou anterior a `dtFimPrev`; nas abertas, é `dtFimPrev` igual ou posterior ao momento da consulta.

## 2. Definição usada

Decisão do produto:

- **Estourou o prazo:** `dtFimPrev` anterior a `dtFimReal` (encerradas) ou ao momento da consulta (abertas). A conta lê as datas; a flag `Req.flgForaSLA` é gravada pelo plano de alertas, onde retrata o último evento dele, e regravada com 0 por uma atualização de versão do produto ([Prioridade e SLA](../dimensoes/prioridade-sla.md)).
- **Canceladas ficam fora do denominador:** a receita descarta o status de código `CL` (cancelada, `Status.cdSta`).
- O grupo é o grupo atual (`idGruAtual`), lido como em [Requisições do grupo atual](requisicoes-do-grupo-atual.md); a requisição sem grupo atual aparece numa linha de grupo vazio.
- As encerradas entram pelo período de `dtFimReal`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta das encerradas devolve vazio (a das abertas não tem filtro de data). O status vem do código `FormStatus.idSta` → `Status.cdSta`. A soma é convertida em `decimal(18,4)` antes da divisão, e a proporção sai com quatro casas decimais (`decimal(9,4)`, arredondada pelo `CAST` externo).

Encerradas:

```sql
SELECT g.idGru, g.dsGru,
       COUNT(*) AS qtd_encerradas,
       SUM(CASE WHEN c.dtFimReal <= c.dtFimPrev THEN 1 ELSE 0 END) AS qtd_no_prazo,
       CAST(CAST(SUM(CASE WHEN c.dtFimReal <= c.dtFimPrev THEN 1 ELSE 0 END) AS decimal(18,4)) / COUNT(*) AS decimal(9,4)) AS proporcao_no_prazo
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = c.idGruAtual
WHERE ISNULL(s.cdSta, '') <> 'CL'
  AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
GROUP BY g.idGru, g.dsGru
ORDER BY g.dsGru;
```

Granularidade do resultado: uma linha por grupo.

Abertas, no momento da consulta:

```sql
SELECT g.idGru, g.dsGru,
       COUNT(*) AS qtd_abertas,
       SUM(CASE WHEN r.dtFimPrev >= GETDATE() THEN 1 ELSE 0 END) AS qtd_no_prazo,
       CAST(CAST(SUM(CASE WHEN r.dtFimPrev >= GETDATE() THEN 1 ELSE 0 END) AS decimal(18,4)) / COUNT(*) AS decimal(9,4)) AS proporcao_no_prazo
FROM Req r WITH(NOLOCK)
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = r.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = r.idGruAtual
WHERE ISNULL(s.cdSta, '') <> 'CL'
GROUP BY g.idGru, g.dsGru
ORDER BY g.dsGru;
```

Granularidade do resultado: uma linha por grupo.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idGru | dsGru | qtd_encerradas | qtd_no_prazo | proporcao_no_prazo |
    |---|---|---|---|---|
    | 9001 | Grupo Exemplo A | 200 | 180 | 0.9000 |
    | 9002 | Grupo Exemplo B | 50 | 40 | 0.8000 |

## 5. Regras aplicadas

- [R-marcos-02](../fatos/marcos.md): "estourou o prazo" compara `dtFimPrev` com `dtFimReal` (encerradas) ou com o momento da consulta (abertas).
- [R-marcos-03](../fatos/marcos.md): `dtFimReal` só existe nas encerradas.
- [R-requisicao-05](../fatos/requisicao.md): o grupo atual é `idGruAtual`.

## Veja também

- [Marcos da requisição](../fatos/marcos.md)
- [Receita: atrasadas agora](atrasadas-agora.md)
- [Prioridade e SLA](../dimensoes/prioridade-sla.md)
