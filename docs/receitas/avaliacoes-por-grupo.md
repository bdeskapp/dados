---
gerado: sincronizacao
---
# Receita: avaliações por grupo


## 1. Pergunta e indicador

- **Pergunta:** como os grupos foram avaliados, e qual a parcela das encerradas não canceladas que recebeu avaliação?
- **Indicadores:**
  - distribuição = número de requisições avaliadas por grupo e por nota (`opAvaliacao`);
  - taxa de resposta = avaliadas dividido pelas encerradas do grupo que não foram canceladas, apresentada à parte;
  - taxa de nota entre os registros = avaliadas dividido pelas encerradas do grupo que têm linha em `ReqAvaliacao`, apresentada ao lado.

## 2. Definição usada

- Satisfação é calculada só sobre as requisições avaliadas, isto é, com `opAvaliacao` preenchido; as não avaliadas entram apenas na taxa de resposta (decisão do produto).
- Uma linha de `ReqAvaliacao` sem nota não conta como avaliada. A nota é o código numérico gravado pelo produto e a receita a apresenta como contagem por código, sem média.
- O grupo é o grupo atual da encerrada, `ReqConcluida.idGruAtual` (o último valor, ver [Fato: requisição](../fatos/requisicao.md)); o nome vem de `Grupo.dsGru` por `LEFT JOIN`. O período filtra `dtFimReal`.
- As receitas cobrem as encerradas. Uma avaliação ainda ligada a uma requisição aberta fica fora.
- Os dois denominadores da taxa:
  - taxa_resposta divide as avaliadas pelas encerradas do grupo, sem as canceladas (status de código `CL`, `FormStatus.idSta` → `Status.cdSta`), o mesmo recorte de [SLA por grupo](sla-por-grupo.md), por decisão do produto. Responde "das encerradas que não foram canceladas, quantas receberam nota".
  - taxa_nota_entre_registros divide as avaliadas pelas encerradas que têm linha em `ReqAvaliacao` (com ou sem nota). Responde "dos registros de avaliação gravados, quantos trazem nota"; o grupo sem nenhuma linha em `ReqAvaliacao` fica com essa taxa vazia.
- A distribuição usa o mesmo recorte: encerradas no período, sem as canceladas (decisão do produto).
- `ReqAvaliacao` tem no máximo uma linha por requisição ([Fato: avaliação e satisfação](../fatos/avaliacao-satisfacao.md)), então o `LEFT JOIN` não repete encerradas.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. Receitas só de encerradas.

Distribuição das avaliadas por grupo e nota:

```sql
SELECT y.idGruAtual, g.dsGru, y.opAvaliacao, COUNT(*) AS qtd_avaliadas
FROM (
    SELECT c.idReq, c.idGruAtual, a.opAvaliacao
    FROM ReqConcluida c WITH(NOLOCK)
        JOIN ReqAvaliacao a WITH(NOLOCK) ON a.idReq = c.idReq
        LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
        LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    WHERE a.opAvaliacao IS NOT NULL
        AND ISNULL(s.cdSta, '') <> 'CL'
        AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
) y
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = y.idGruAtual
GROUP BY y.idGruAtual, g.dsGru, y.opAvaliacao;
```

Granularidade do resultado: uma linha por grupo e nota.

Taxa de resposta por grupo, à parte da distribuição:

```sql
SELECT c.idGruAtual, g.dsGru,
    COUNT(*) AS qtd_encerradas,
    COUNT(a.idReq) AS qtd_com_registro_avaliacao,
    SUM(CASE WHEN a.opAvaliacao IS NOT NULL THEN 1 ELSE 0 END) AS qtd_avaliadas,
    CAST(SUM(CASE WHEN a.opAvaliacao IS NOT NULL THEN 1 ELSE 0 END) AS float) / COUNT(*) AS taxa_resposta,
    CAST(SUM(CASE WHEN a.opAvaliacao IS NOT NULL THEN 1 ELSE 0 END) AS float) / NULLIF(COUNT(a.idReq), 0) AS taxa_nota_entre_registros
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN ReqAvaliacao a WITH(NOLOCK) ON a.idReq = c.idReq
    LEFT JOIN FormStatus fs WITH(NOLOCK) ON fs.idFrmStatus = c.idFrmStatus
    LEFT JOIN Status s WITH(NOLOCK) ON s.idSta = fs.idSta
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = c.idGruAtual
WHERE ISNULL(s.cdSta, '') <> 'CL'
    AND c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0
GROUP BY c.idGruAtual, g.dsGru;
```

Granularidade do resultado: uma linha por grupo atual. qtd_encerradas já exclui as canceladas. taxa_resposta é a fração de avaliadas entre essas encerradas; taxa_nota_entre_registros é a fração de avaliadas entre as que têm linha em `ReqAvaliacao`.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    **exemplo fictício** (taxa de resposta)

    | idGruAtual | dsGru | qtd_encerradas | qtd_com_registro_avaliacao | qtd_avaliadas | taxa_resposta | taxa_nota_entre_registros |
    |---|---|---|---|---|---|---|
    | 9001 | Grupo Exemplo A | 200 | 50 | 40 | 0.2 | 0.8 |
    | 9002 | Grupo Exemplo B | 80 | 0 | 0 | 0 | |

## 5. Regras aplicadas

- [R-avaliacao-satisfacao-01](../fatos/avaliacao-satisfacao.md): calcule satisfação só sobre as avaliadas.
- [R-avaliacao-satisfacao-02](../fatos/avaliacao-satisfacao.md): apresente a taxa de resposta à parte; aqui o denominador são as encerradas do recorte sem as canceladas.
- [R-avaliacao-satisfacao-03](../fatos/avaliacao-satisfacao.md): `opAvaliacao` é um código; apresente a distribuição por código.

## Veja também

- [Fato: avaliação e satisfação](../fatos/avaliacao-satisfacao.md)
- [Fato: requisição](../fatos/requisicao.md)
