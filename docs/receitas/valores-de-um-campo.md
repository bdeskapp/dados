---
gerado: sincronizacao
---
# Receita: valores de um campo nas requisições


## 1. Pergunta e indicador

- **Pergunta:** que valor cada requisição, aberta ou encerrada, tem num determinado dado adicional?
- **Indicador:** lista de valores = uma linha por valor do campo em cada requisição (e por item escolhido, quando o campo é de lista).

## 2. Definição usada

- O campo é escolhido por `DadContextoCampo.idDad`; o campo pode ter vários contextos, e todos entram, um valor por contexto (decisão do produto; [Dados adicionais](../fatos/dados-adicionais.md), R-dados-adicionais-03). A coluna n_ctx traz em quantos contextos o campo tem valor naquela requisição e `nSeq`.
- A requisição é `DadValor.idQQ` com `DadContextoCampo.idEnt = 3` (Requisição, em [Valores definidos pelo produto](../dominios-do-produto.md); R-dados-adicionais-01) e `flgAgenda = 0` (R-dados-adicionais-07).
- O valor sai na coluna que o `tpDado` do campo indica. Ao inserir e ao alterar um valor, o produto escreve só a coluna do `tpDado` que o campo tem naquele momento e não limpa as outras. A receita devolve as seis colunas lado a lado para mostrar também um valor que esteja fora da coluna do `tpDado` atual. Em campo de lista (`tpDado = 8`), `idDom` e `dsDom` trazem o item.
- Nenhum filtro de contexto ativo: o valor gravado é lido mesmo quando o contexto foi desativado depois (R-dados-adicionais-06).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro do id do campo, que vem com `0` como placeholder fictício (substitua o `0` pelo id do campo); `WITH(NOLOCK)`. O primeiro ramo é o das abertas e o segundo o das encerradas; para um estado só, mantenha o ramo correspondente.

```sql
SELECT v.idQQ AS idReq, 1 AS flg_aberta, r.idFrm, v.idDadCon, v.nSeq,
       v.string, v.numero, v.data, v.boolean, v.dinheiro,
       CAST(v.texto AS VARCHAR(MAX)) AS texto,
       dd.idDom, dd.dsDom,
       (SELECT COUNT(DISTINCT v2.idDadCon) FROM DadValor v2 WITH(NOLOCK)
        INNER JOIN DadContextoCampo c2 WITH(NOLOCK) ON c2.idDadCon = v2.idDadCon
        WHERE v2.idQQ = v.idQQ AND v2.nSeq = v.nSeq AND v2.flgAgenda = 0
          AND c2.idEnt = 3 AND c2.idDad = c.idDad) AS n_ctx
FROM DadValor v WITH(NOLOCK)
INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
INNER JOIN Req r WITH(NOLOCK) ON r.idReq = v.idQQ
LEFT JOIN DadValorDominio dvd WITH(NOLOCK) ON dvd.idDadVal = v.idDadVal
LEFT JOIN DadDominio dd WITH(NOLOCK) ON dd.idDom = dvd.idDom
WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
UNION ALL
SELECT v.idQQ, 0, rc.idFrm, v.idDadCon, v.nSeq,
       v.string, v.numero, v.data, v.boolean, v.dinheiro,
       CAST(v.texto AS VARCHAR(MAX)),
       dd.idDom, dd.dsDom,
       (SELECT COUNT(DISTINCT v2.idDadCon) FROM DadValor v2 WITH(NOLOCK)
        INNER JOIN DadContextoCampo c2 WITH(NOLOCK) ON c2.idDadCon = v2.idDadCon
        WHERE v2.idQQ = v.idQQ AND v2.nSeq = v.nSeq AND v2.flgAgenda = 0
          AND c2.idEnt = 3 AND c2.idDad = c.idDad)
FROM DadValor v WITH(NOLOCK)
INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
INNER JOIN ReqConcluida rc WITH(NOLOCK) ON rc.idReq = v.idQQ
LEFT JOIN DadValorDominio dvd WITH(NOLOCK) ON dvd.idDadVal = v.idDadVal
LEFT JOIN DadDominio dd WITH(NOLOCK) ON dd.idDom = dvd.idDom
WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0;
```

Granularidade do resultado: uma linha por valor (`idDadCon` + `nSeq` por requisição) e, em campo de lista, por item escolhido.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    **exemplo fictício** (campo de texto)

    | idReq | flg_aberta | idFrm | idDadCon | nSeq | string | dsDom | n_ctx |
    |---|---|---|---|---|---|---|---|
    | 9000001 | 1 | 9001 | 9101 | 1 | Valor Exemplo A | | 1 |
    | 9000002 | 0 | 9001 | 9101 | 1 | Valor Exemplo B | | 1 |

## 5. Regras aplicadas

- [R-dados-adicionais-01](../fatos/dados-adicionais.md): ligue por `idQQ` e filtre `idEnt = 3`.
- [R-dados-adicionais-02](../fatos/dados-adicionais.md): junte com `Req` e `ReqConcluida`.
- [R-dados-adicionais-04](../fatos/dados-adicionais.md): a coluna do valor depende do `tpDado`.

## Veja também

- [Fato: dados adicionais](../fatos/dados-adicionais.md)
- [Pivô de campos](pivo-de-campos.md)
