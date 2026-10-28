---
gerado: sincronizacao
---
# Receita: formulários que usam um campo


## 1. Pergunta e indicador

- **Pergunta:** em que formulários um dado adicional está configurado, e em quais deles ele tem valor preenchido?
- **Indicador:** contextos do campo = uma linha por contexto (onde o campo vale); formulários com valor = requisições distintas com valor, por formulário.

## 2. Definição usada

- Cada contexto de requisição (`DadContextoCampo` com `idEnt = 3`) guarda o escopo em cinco colunas: formulário (`idFrm`), atividade (`idTar`), subcategoria (`idSca`), categoria (`idCat`) ou área (`idAre`). A tabela aceita mais de uma preenchida e um mesmo contexto pode ter `idFrm` e a área preenchidos ao mesmo tempo; por isso leia as cinco colunas de cada contexto ([Dados adicionais](../fatos/dados-adicionais.md), R-dados-adicionais-10). O primeiro bloco lista os contextos de requisição do campo com as cinco colunas de escopo; `idFrm` leva ao `Formulario`.
- Contextos de atividade, subcategoria, categoria e área valem para a classificação; o formulário em que o campo aparece é o da requisição. Em valores de contexto de formulário, o `idFrm` do contexto pode diferir do `idFrm` da requisição; a receita traz os dois, sem decidir qual formulário vale. O segundo bloco conta as requisições com valor por `idFrm` da requisição, abertas e encerradas.
- `flgContextoAtivo` diz se o contexto está ativo para novos preenchimentos e `Formulario.flgFrmAtivo` se o formulário está ativo; o segundo bloco não filtra por eles, para trazer também os valores de contextos já desativados (R-dados-adicionais-06).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro do id do campo, que vem com `0` como placeholder fictício (substitua o `0` pelo id do campo); `WITH(NOLOCK)`. O primeiro bloco é do cadastro, sem requisições. O segundo traz um ramo de abertas e um de encerradas.

```sql
SELECT c.idDadCon,
       c.idFrm, c.idTar, c.idSca, c.idCat, c.idAre,
       f.dsFrm, f.flgFrmAtivo, c.idCon, c.flgContextoAtivo
FROM DadContextoCampo c WITH(NOLOCK)
LEFT JOIN Formulario f WITH(NOLOCK) ON f.idFrm = c.idFrm
WHERE c.idEnt = 3 AND c.idDad = /* @idDad */ 0;
```

```sql
SELECT x.idFrm, f.dsFrm, f.flgFrmAtivo,
       SUM(CASE WHEN x.flg_aberta = 1 THEN x.qtd ELSE 0 END) AS qtd_abertas,
       SUM(CASE WHEN x.flg_aberta = 0 THEN x.qtd ELSE 0 END) AS qtd_encerradas
FROM (
    SELECT r.idFrm, 1 AS flg_aberta, COUNT(DISTINCT v.idQQ) AS qtd
    FROM DadValor v WITH(NOLOCK)
    INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
    INNER JOIN Req r WITH(NOLOCK) ON r.idReq = v.idQQ
    WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
    GROUP BY r.idFrm
    UNION ALL
    SELECT rc.idFrm, 0, COUNT(DISTINCT v.idQQ)
    FROM DadValor v WITH(NOLOCK)
    INNER JOIN DadContextoCampo c WITH(NOLOCK) ON c.idDadCon = v.idDadCon
    INNER JOIN ReqConcluida rc WITH(NOLOCK) ON rc.idReq = v.idQQ
    WHERE c.idEnt = 3 AND v.flgAgenda = 0 AND c.idDad = /* @idDad */ 0
    GROUP BY rc.idFrm
) x
LEFT JOIN Formulario f WITH(NOLOCK) ON f.idFrm = x.idFrm
GROUP BY x.idFrm, f.dsFrm, f.flgFrmAtivo;
```

Granularidade dos resultados: o primeiro, uma linha por contexto (`idDadCon`); o segundo, uma linha por formulário.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    **exemplo fictício** (segundo bloco)

    | idFrm | dsFrm | flgFrmAtivo | qtd_abertas | qtd_encerradas |
    |---|---|---|---|---|
    | 9001 | Formulário Exemplo A | 1 | 8 | 410 |
    | 9002 | Formulário Exemplo B | 0 | 0 | 56 |

## 5. Regras aplicadas

- [R-dados-adicionais-06](../fatos/dados-adicionais.md): `flgContextoAtivo` (contexto) e `flgDadAtivo` (campo) são colunas diferentes; o valor gravado é lido sem esse filtro.
- [R-dados-adicionais-10](../fatos/dados-adicionais.md): escopo do contexto mais formulário da requisição.

## Veja também

- [Fato: dados adicionais](../fatos/dados-adicionais.md)
- [Valores de um campo](valores-de-um-campo.md)
