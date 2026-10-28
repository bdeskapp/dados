---
gerado: sincronizacao
---
# Receita: distribuição de um campo de lista


## 1. Pergunta e indicador

- **Pergunta:** quantas requisições escolheram cada item de um campo de lista?
- **Indicador:** requisições por item = número de requisições distintas (`idQQ`) com aquele item (`idDom`) escolhido, separadas em abertas e encerradas.

## 2. Definição usada

- O campo de lista é um `DadoAdicional` com `tpDado = 8`; os itens escolhidos ficam em `DadValorDominio` (uma linha por item) e o texto do item é `DadDominio.dsDom` ([Dados adicionais](../fatos/dados-adicionais.md), R-dados-adicionais-05).
- A contagem é de requisições distintas por `idQQ`: uma requisição com várias repetições (`nSeq`) ou contextos conta uma vez por item. A contagem é por requisição; a contagem de contextos fica em n_contextos. Uma requisição com dois itens conta em cada um, e a soma da coluna pode passar do número de requisições.
- A lista parte de `DadDominio` do campo, e os itens sem escolha aparecem com zero. A contagem deixa de fora dois grupos: valores que apontam para item de outro campo (dado inconsistente, decisão do produto) e valores de lista sem nenhum item em `DadValorDominio` (valor vazio). `flgDomAtivo` mostra se o item está ativo no cadastro. O campo pode ter valores em mais de um contexto (`idDadCon`), e todos entram, um por contexto (decisão do produto); n_contextos traz em quantos contextos o item foi escolhido.
- Filtros do valor: `idEnt = 3` e `flgAgenda = 0` (R-dados-adicionais-01 e 07). Abertas e encerradas são contadas à parte e somadas em qtd_total, porque `Req` e `ReqConcluida` não têm `idReq` em comum.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro do id do campo de lista, que vem com `0` como placeholder fictício (substitua o `0` pelo id do campo); `WITH(NOLOCK)`. As duas primeiras subconsultas contam, respectivamente, as abertas e as encerradas, e a terceira (`x`) conta os contextos nas duas tabelas; para um estado só, mantenha a coluna correspondente; n_contextos mistura `Req` e `ReqConcluida` e não acompanha esse recorte.

```sql
SELECT dd.idDom, dd.dsDom, dd.flgDomAtivo,
       ISNULL(a.qtd, 0) AS qtd_abertas,
       ISNULL(e.qtd, 0) AS qtd_encerradas,
       ISNULL(a.qtd, 0) + ISNULL(e.qtd, 0) AS qtd_total,
       ISNULL(x.n_ctx, 0) AS n_contextos
FROM DadDominio dd WITH(NOLOCK)
LEFT JOIN (
    SELECT dvd.idDom, COUNT(DISTINCT v.idQQ) AS qtd
    FROM DadValor v WITH(NOLOCK)
    INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
    INNER JOIN Req r WITH(NOLOCK) ON r.idReq = v.idQQ
    INNER JOIN DadValorDominio dvd WITH(NOLOCK) ON dvd.idDadVal = v.idDadVal
    WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
    GROUP BY dvd.idDom
) a ON a.idDom = dd.idDom
LEFT JOIN (
    SELECT dvd.idDom, COUNT(DISTINCT v.idQQ) AS qtd
    FROM DadValor v WITH(NOLOCK)
    INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
    INNER JOIN ReqConcluida rc WITH(NOLOCK) ON rc.idReq = v.idQQ
    INNER JOIN DadValorDominio dvd WITH(NOLOCK) ON dvd.idDadVal = v.idDadVal
    WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
    GROUP BY dvd.idDom
) e ON e.idDom = dd.idDom
LEFT JOIN (
    SELECT dvd.idDom, COUNT(DISTINCT v.idDadCon) AS n_ctx
    FROM DadValor v WITH(NOLOCK)
    INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
    INNER JOIN DadValorDominio dvd WITH(NOLOCK) ON dvd.idDadVal = v.idDadVal
    WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
      AND (EXISTS (SELECT 1 FROM Req r WITH(NOLOCK) WHERE r.idReq = v.idQQ)
        OR EXISTS (SELECT 1 FROM ReqConcluida rc WITH(NOLOCK) WHERE rc.idReq = v.idQQ))
    GROUP BY dvd.idDom
) x ON x.idDom = dd.idDom
WHERE dd.idDad = /* @idDad */ 0;
```

Granularidade do resultado: uma linha por item da lista.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idDom | dsDom | flgDomAtivo | qtd_abertas | qtd_encerradas | qtd_total | n_contextos |
    |---|---|---|---|---|---|---|
    | 9501 | Item Exemplo A | 1 | 12 | 340 | 352 | 2 |
    | 9502 | Item Exemplo B | 1 | 4 | 87 | 91 | 1 |
    | 9503 | Item Exemplo C | 0 | 0 | 15 | 15 | 1 |

## 5. Regras aplicadas

- [R-dados-adicionais-05](../fatos/dados-adicionais.md): itens em `DadValorDominio`, rótulo em `dsDom`, `COUNT(DISTINCT idQQ)`.
- [R-dados-adicionais-02](../fatos/dados-adicionais.md): abertas e encerradas contadas pelos dois lados.

## Veja também

- [Fato: dados adicionais](../fatos/dados-adicionais.md)
- [Valores de um campo](valores-de-um-campo.md)
