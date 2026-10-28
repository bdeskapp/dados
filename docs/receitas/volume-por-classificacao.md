---
gerado: sincronizacao
---
# Receita: volume de requisições por categoria, subcategoria e atividade


## 1. Pergunta e indicador

- **Pergunta:** por estado (abertas e encerradas lado a lado), quantas requisições foram abertas em cada categoria, subcategoria e atividade?
- **Indicador:** volume = número de requisições cuja data de abertura (`dtAbertura`) cai no período, agrupadas por categoria, subcategoria e atividade.

## 2. Definição usada

- **Aberta:** a classificação vem do cadastro **atual**. `Req` guarda só a atividade (`idTar`); a categoria da atividade é `Tarefa.idCat` e a subcategoria é `Tarefa.idSca`, o mesmo par que o retrato da encerrada usa (R-classificacao-01). A ligação é `LEFT JOIN`, e a requisição sem atividade aparece com sem_atividade = 1 e as colunas de categoria, subcategoria e atividade vazias (R-classificacao-02).
- **Encerrada:** a classificação vem do **retrato** gravado em `ReqConcluida` no encerramento (`idCat`, `dsCat`, `idSca`, `dsSca`, `idTar`, `dsTar`) (R-classificacao-03). Os rótulos são os gravados no encerramento; um script pontual reescreve `dsCat`, `dsSca` e `dsTar` de parte das encerradas com os rótulos do cadastro atual. `idCat` e `idSca` também são retrato: uma atividade pode ter mudado de subcategoria ou de categoria entre encerramentos, e ids diferentes para o mesmo `idTar` geram linhas diferentes. A receita agrupa pelos ids (`idCat`, `idSca`, `idTar`); rótulos diferentes gravados com os mesmos ids caem na mesma linha, e o rótulo mostrado é o maior entre as grafias em ordem binária, que distingue acento e maiúscula e por isso escolhe sempre a mesma grafia. O total por atividade soma as linhas por `idTar`; o total por categoria soma por `idCat`.
- **Variante combinada:** uma linha por estado × categoria × subcategoria × atividade. A coluna `encerrada` (0 = aberta, 1 = encerrada) mostra a fonte de cada lado: cadastro atual (aberta) ou retrato (encerrada). Os dois lados não são somados entre si, porque as fontes dos rótulos são diferentes.
- O período é o de `dtAbertura`, preenchida nas duas tabelas. O estado atual da requisição não entra no filtro.
- Volume = abertas + encerradas: `Req` e `ReqConcluida` não têm `idReq` em comum ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetros como placeholders fictícios; `WITH(NOLOCK)`. Nos parâmetros de data (início e fim do período), o `0` só serve para a consulta compilar; substitua o `0` de cada parâmetro por uma data, por exemplo `'2030-01-01'`, antes de rodar, porque com `0` a consulta devolve vazio. Três variantes: só abertas, só encerradas e as duas juntas.

Só abertas (cadastro atual):

```sql
SELECT c.idCat, MAX(c.dsCat COLLATE Latin1_General_BIN2) AS dsCat, s.idSca, MAX(s.dsSca COLLATE Latin1_General_BIN2) AS dsSca, t.idTar,
       MAX(t.dsTar COLLATE Latin1_General_BIN2) AS dsAtividade, CASE WHEN t.idTar IS NULL THEN 1 ELSE 0 END AS sem_atividade,
       COUNT(*) AS qtd_requisicoes
FROM Req r WITH(NOLOCK)
LEFT JOIN Tarefa t WITH(NOLOCK) ON t.idTar = r.idTar
LEFT JOIN SubCategoria s WITH(NOLOCK) ON s.idSca = t.idSca
LEFT JOIN Categoria c WITH(NOLOCK) ON c.idCat = t.idCat
WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
GROUP BY c.idCat, s.idSca, t.idTar
ORDER BY dsCat, dsSca, dsAtividade;
```

Só encerradas (retrato do encerramento):

```sql
SELECT c.idCat, MAX(c.dsCat COLLATE Latin1_General_BIN2) AS dsCat, c.idSca, MAX(c.dsSca COLLATE Latin1_General_BIN2) AS dsSca, c.idTar,
       MAX(c.dsTar COLLATE Latin1_General_BIN2) AS dsAtividade, CASE WHEN c.idTar IS NULL THEN 1 ELSE 0 END AS sem_atividade,
       COUNT(*) AS qtd_requisicoes
FROM ReqConcluida c WITH(NOLOCK)
WHERE c.dtAbertura >= /* @dtInicio */ 0 AND c.dtAbertura < /* @dtFim */ 0
GROUP BY c.idCat, c.idSca, c.idTar
ORDER BY dsCat, dsSca, dsAtividade;
```

Abertas e encerradas, com a coluna `encerrada` (0 = aberta, 1 = encerrada):

```sql
SELECT x.encerrada, x.idCat, x.dsCat, x.idSca, x.dsSca, x.idTar, x.dsAtividade, x.sem_atividade, x.qtd_requisicoes
FROM (
    SELECT 0 AS encerrada, c.idCat, MAX(c.dsCat COLLATE Latin1_General_BIN2) AS dsCat, s.idSca, MAX(s.dsSca COLLATE Latin1_General_BIN2) AS dsSca, t.idTar,
           MAX(t.dsTar COLLATE Latin1_General_BIN2) AS dsAtividade, CASE WHEN t.idTar IS NULL THEN 1 ELSE 0 END AS sem_atividade,
           COUNT(*) AS qtd_requisicoes
    FROM Req r WITH(NOLOCK)
    LEFT JOIN Tarefa t WITH(NOLOCK) ON t.idTar = r.idTar
    LEFT JOIN SubCategoria s WITH(NOLOCK) ON s.idSca = t.idSca
    LEFT JOIN Categoria c WITH(NOLOCK) ON c.idCat = t.idCat
    WHERE r.dtAbertura >= /* @dtInicio */ 0 AND r.dtAbertura < /* @dtFim */ 0
    GROUP BY c.idCat, s.idSca, t.idTar
    UNION ALL
    SELECT 1, e.idCat, MAX(e.dsCat COLLATE Latin1_General_BIN2), e.idSca, MAX(e.dsSca COLLATE Latin1_General_BIN2), e.idTar,
           MAX(e.dsTar COLLATE Latin1_General_BIN2), CASE WHEN e.idTar IS NULL THEN 1 ELSE 0 END,
           COUNT(*)
    FROM ReqConcluida e WITH(NOLOCK)
    WHERE e.dtAbertura >= /* @dtInicio */ 0 AND e.dtAbertura < /* @dtFim */ 0
    GROUP BY e.idCat, e.idSca, e.idTar
) x
ORDER BY x.encerrada, x.dsCat, x.dsSca, x.dsAtividade;
```

Granularidade do resultado: uma linha por categoria × subcategoria × atividade (e por `encerrada`, na variante combinada). Nas encerradas, uma linha por combinação distinta de ids gravados; some por `idTar` (atividade) ou por `idCat` (categoria) para os totais.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | encerrada | idCat | dsCat | idSca | dsSca | idTar | dsAtividade | sem_atividade | qtd_requisicoes |
    |---|---|---|---|---|---|---|---|---|
    | 0 | 9001 | Categoria Exemplo A | 9101 | Subcategoria Exemplo A1 | 9201 | Atividade Exemplo A1a | 0 | 40 |
    | 0 | | | | | | | 1 | 12 |
    | 1 | 9001 | Categoria Exemplo A | 9101 | Subcategoria Exemplo A1 | 9201 | Atividade Exemplo A1a | 0 | 75 |

## 5. Regras aplicadas

- [R-classificacao-01](../dimensoes/classificacao.md): a categoria da atividade é `Tarefa.idCat` e a subcategoria é `Tarefa.idSca`.
- [R-classificacao-02](../dimensoes/classificacao.md): ligue `Req.idTar` a `Tarefa` com `LEFT JOIN`.
- [R-classificacao-03](../dimensoes/classificacao.md): leia a classificação de uma encerrada no retrato de `ReqConcluida`.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas para qualquer volume histórico.

## Veja também

- [Dimensão: classificação](../dimensoes/classificacao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Receita: volume por mês](volume-por-mes.md)
