---
gerado: sincronizacao
---
# Receita: vários campos como colunas, uma linha por requisição


## 1. Pergunta e indicador

- **Pergunta:** como ver os valores de vários dados adicionais lado a lado, um campo por coluna?
- **Indicador:** pivô = para cada requisição (e repetição `nSeq`), o valor de cada campo escolhido e a quantidade de contextos em que o campo tem valor.

## 2. Definição usada

- Cada campo é uma coluna do resultado, com o valor do campo escolhido agregado por requisição e repetição. A coluna do valor depende do `tpDado` do campo ([Dados adicionais](../fatos/dados-adicionais.md), R-dados-adicionais-04). O exemplo traz cinco campos: texto curto (`string`), numérico (`numero`), data (`data`), booleano (`boolean`) e texto longo (`texto`). O `MAX` não aceita `bit` nem `TEXT`, então o booleano entra convertido em inteiro e o texto longo convertido em texto de tamanho máximo; troque a coluna conforme o tipo de cada campo, no `MAX` e no `COUNT` do par.
- A linha é por requisição e `nSeq` (R-dados-adicionais-08). `nSeq` numera as repetições de um conjunto (`DadContextoCampo.idCon`), então esta linha só faz sentido para campos do mesmo conjunto, ou para campos fora de conjunto múltiplo (que têm `nSeq = 1`). Campos de conjuntos diferentes pedem um pivô por conjunto: juntos, as repetições de um conjunto ficam em linhas separadas das do outro. Filtrar `nSeq` igual a 1 leva a uma linha por requisição, e descarta as repetições (`nSeq > 1`).
- A contagem de contextos, nas colunas n_ctx_campo1, n_ctx_campo2 e seguintes, mostra em quantos contextos o campo tem valor naquela requisição: a linha de `DadValor` entra só quando a coluna do valor do campo não é `NULL` (`COUNT` da própria coluna); um texto vazio conta como valor. Quando passa de 1, o valor mostrado é o maior entre os contextos e os demais ficam na receita [valores de um campo](valores-de-um-campo.md) (R-dados-adicionais-09). Cada contexto vale, com um valor por contexto (decisão do produto), e por isso a contagem aparece ao lado do valor.
- Campo de lista (`tpDado = 8`) tem os itens em `DadValorDominio`; a receita [distribuição de um campo de lista](distribuicao-campo-lista.md) e a de valores de um campo trazem os itens.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros dos ids dos campos (cinco no exemplo), que vêm com `0` como placeholders fictícios (substitua cada `0` pelo id de um campo); `WITH(NOLOCK)`. O primeiro ramo é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente. Para mais campos, repita o par de colunas e inclua o `idDad` no `IN`; as colunas n_ctx_campo2 a n_ctx_campo5 seguem o mesmo formato de n_ctx_campo1 e foram omitidas do exemplo.

```sql
SELECT v.idQQ AS idReq, 1 AS flg_aberta, v.nSeq,
       MAX(CASE WHEN c.idDad = /* @idDad1 */ 0 THEN v.string END) AS campo1,
       COUNT(CASE WHEN c.idDad = /* @idDad1 */ 0 THEN v.string END) AS n_ctx_campo1,
       MAX(CASE WHEN c.idDad = /* @idDad2 */ 0 THEN v.numero END) AS campo2,
       COUNT(CASE WHEN c.idDad = /* @idDad2 */ 0 THEN v.numero END) AS n_ctx_campo2,
       MAX(CASE WHEN c.idDad = /* @idDad3 */ 0 THEN v.data END) AS campo3,
       COUNT(CASE WHEN c.idDad = /* @idDad3 */ 0 THEN v.data END) AS n_ctx_campo3,
       MAX(CAST(CASE WHEN c.idDad = /* @idDad4 */ 0 THEN v.boolean END AS INT)) AS campo4,
       COUNT(CASE WHEN c.idDad = /* @idDad4 */ 0 THEN v.boolean END) AS n_ctx_campo4,
       MAX(CAST(CASE WHEN c.idDad = /* @idDad5 */ 0 THEN v.texto END AS VARCHAR(MAX))) AS campo5,
       COUNT(CASE WHEN c.idDad = /* @idDad5 */ 0 THEN CAST(v.texto AS VARCHAR(MAX)) END) AS n_ctx_campo5
FROM DadValor v WITH(NOLOCK)
INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
INNER JOIN Req r WITH(NOLOCK) ON r.idReq = v.idQQ
WHERE c.idEnt = 3 AND v.flgAgenda = 0
  AND c.idDad IN (/* @idDad1 */ 0, /* @idDad2 */ 0, /* @idDad3 */ 0, /* @idDad4 */ 0, /* @idDad5 */ 0)
GROUP BY v.idQQ, v.nSeq
UNION ALL
SELECT v.idQQ, 0, v.nSeq,
       MAX(CASE WHEN c.idDad = /* @idDad1 */ 0 THEN v.string END),
       COUNT(CASE WHEN c.idDad = /* @idDad1 */ 0 THEN v.string END),
       MAX(CASE WHEN c.idDad = /* @idDad2 */ 0 THEN v.numero END),
       COUNT(CASE WHEN c.idDad = /* @idDad2 */ 0 THEN v.numero END),
       MAX(CASE WHEN c.idDad = /* @idDad3 */ 0 THEN v.data END),
       COUNT(CASE WHEN c.idDad = /* @idDad3 */ 0 THEN v.data END),
       MAX(CAST(CASE WHEN c.idDad = /* @idDad4 */ 0 THEN v.boolean END AS INT)),
       COUNT(CASE WHEN c.idDad = /* @idDad4 */ 0 THEN v.boolean END),
       MAX(CAST(CASE WHEN c.idDad = /* @idDad5 */ 0 THEN v.texto END AS VARCHAR(MAX))),
       COUNT(CASE WHEN c.idDad = /* @idDad5 */ 0 THEN CAST(v.texto AS VARCHAR(MAX)) END)
FROM DadValor v WITH(NOLOCK)
INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
INNER JOIN ReqConcluida rc WITH(NOLOCK) ON rc.idReq = v.idQQ
WHERE c.idEnt = 3 AND v.flgAgenda = 0
  AND c.idDad IN (/* @idDad1 */ 0, /* @idDad2 */ 0, /* @idDad3 */ 0, /* @idDad4 */ 0, /* @idDad5 */ 0)
GROUP BY v.idQQ, v.nSeq;
```

Granularidade do resultado: uma linha por requisição e `nSeq`.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | flg_aberta | nSeq | campo1 | campo2 | campo3 | campo4 | campo5 | n_ctx_campo1 |
    |---|---|---|---|---|---|---|---|---|
    | 9000001 | 1 | 1 | Valor Exemplo A | 10 | 2030-01-15 | 1 | Texto Exemplo A | 1 |
    | 9000002 | 0 | 1 | Valor Exemplo B | 25 | 2030-02-03 | 0 | Texto Exemplo B | 1 |

## 5. Regras aplicadas

- [R-dados-adicionais-04](../fatos/dados-adicionais.md): a coluna do valor depende do `tpDado`.
- [R-dados-adicionais-08](../fatos/dados-adicionais.md): `nSeq` faz parte da chave.
- [R-dados-adicionais-09](../fatos/dados-adicionais.md): confira a contagem de contextos.

## Veja também

- [Fato: dados adicionais](../fatos/dados-adicionais.md)
- [Valores de um campo](valores-de-um-campo.md)
